#!/usr/bin/env python3
"""
CTS Corp converter
==================
Converts w95/awesome-claude-corporate-skills (Claude SKILL.md collection, MIT)
into two branded skill packs:

  - OpenCode variant : <out>/opencode/<category>/cts-<slug>/SKILL.md
                       (installed to ~/.config/opencode/skills/)
  - Hermes variant   : <out>/hermes/<category>/cts-<slug>/SKILL.md
                       (staged; copy into ~/.hermes/skills/ manually)

Conversion rules:
  * skill id/folder  -> cts-<original folder name>, deduped on collision
  * frontmatter      -> name + description forced; other fields preserved
  * description      -> prefixed with "CTS Corp - "
  * body             -> stray inline `description:` moved to frontmatter,
                        "Claude Code" -> target platform,
                        ~/.claude paths -> platform paths,
                        CTS Corp attribution inserted under the H1
  * hermes extras    -> version: 1.0.0 + metadata.hermes.{category,tags}
"""

import json
import os
import re
import shutil
import sys
from datetime import date

SRC = r"C:\Users\almos\AppData\Local\Temp\opencode\awesome-claude-corporate-skills"
OUT = r"D:\Tools\CTS-Corp"
OC_DEST = os.path.expanduser(r"~\.config\opencode\skills")

BRAND = "CTS Corp"
ATTR = (
    "> **{brand}** \u2014 corporate skill pack for {target}. "
    "Converted from [awesome-claude-corporate-skills]"
    "(https://github.com/w95/awesome-claude-corporate-skills) (MIT)."
)

warnings = []


def warn(msg):
    warnings.append(msg)
    print("WARN:", msg)


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as f:
        raw = f.read()
    nl = "\r\n" if raw.count("\r\n") >= raw.count("\n") - raw.count("\r\n") else "\n"
    return raw.replace("\r\n", "\n"), nl


def write_text(path, text, nl):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text.replace("\n", nl))


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


BLOCK = {"|", "|-", "|+", ">", ">-", ">+"}


def extract_description(fm_lines):
    """Pull description out of a frontmatter line list, removing it in place."""
    for i, line in enumerate(fm_lines):
        m = re.match(r"^description:\s*(.*)$", line)
        if not m:
            continue
        val = m.group(1).strip()
        if val in BLOCK:
            j, chunk = i + 1, []
            while j < len(fm_lines):
                l = fm_lines[j]
                if l.strip() == "" or re.match(r"^\s", l):
                    chunk.append(l.strip())
                    j += 1
                else:
                    break
            del fm_lines[i:j]
            return " ".join(x for x in chunk if x)
        del fm_lines[i]
        return unquote(val)
    return None


def first_paragraph(body):
    paras = re.split(r"\n\s*\n", body)
    for p in paras:
        p = p.strip()
        if not p or p.startswith("#") or p.startswith("```") or p.startswith("---"):
            continue
        return re.sub(r"\s+", " ", p)[:500]
    return None


def process_body(body, slug, target, category):
    # Move stray inline `description:` line into frontmatter (28 skills have this).
    inline = None
    m = re.search(r"^description:\s*(.+)$", body, re.M)
    if m:
        inline = unquote(m.group(1))
        body = body[: m.start()] + body[m.end():]
        body = re.sub(r"\n{3,}", "\n\n", body)

    # Conservative platform retargeting (longest patterns first).
    if target == "OpenCode":
        body = body.replace("Claude Code", "OpenCode")
        body = body.replace("~/.claude/skills", "~/.config/opencode/skills")
        body = body.replace("~/.claude", "~/.config/opencode")
    else:
        body = body.replace("Claude Code", "Hermes")
        body = body.replace("~/.claude/skills", "~/.hermes/skills")
        body = body.replace("~/.claude", "~/.hermes")

    # CTS Corp attribution right under the first H1.
    attr = ATTR.format(brand=BRAND, target=target)
    lines = body.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("# "):
            if i + 1 < len(lines) and lines[i + 1].strip() == "":
                lines[i + 1:i + 2] = ["", attr, ""]
            else:
                lines[i + 1:i + 1] = ["", attr, ""]
            break
    else:
        lines[0:0] = [attr, ""]
    return "\n".join(lines), inline


def build_frontmatter(fm_lines, slug, desc, target, category):
    # drop original name/description keys (description already extracted)
    fm_lines = [l for l in fm_lines if not re.match(r"^name:\s", l)]
    head = ["name: " + slug, "description: " + json.dumps(BRAND + " \u2014 " + desc)]
    if target == "Hermes":
        if not any(re.match(r"^version:\s", l) for l in fm_lines):
            head.append("version: 1.0.0")
        has_meta = any(re.match(r"^metadata:\s*$", l) for l in fm_lines)
        hermes_block = [
            "metadata:",
            "  hermes:",
            "    category: " + category,
            "    tags: [" + category + ", corporate]",
        ]
        if has_meta:
            for i, l in enumerate(fm_lines):
                if re.match(r"^metadata:\s*$", l):
                    fm_lines = fm_lines[: i + 1] + hermes_block[1:] + fm_lines[i + 1:]
                    break
        else:
            fm_lines = fm_lines + hermes_block
    return "---\n" + "\n".join(head + fm_lines) + "\n---\n"


def copy_skill(src_dir, dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(
        src_dir,
        dst_dir,
        ignore=shutil.ignore_patterns("SKILL.md"),
    )


def main():
    if not os.path.isdir(SRC):
        sys.exit("source repo not found: " + SRC)

    # --- parse INDEX.md for per-skill source attribution -------------
    index_map = {}
    idx = os.path.join(SRC, "INDEX.md")
    if os.path.isfile(idx):
        text, _ = read_text(idx)
        for line in text.splitlines():
            m = re.match(r"^\|\s*([a-z0-9][a-z0-9-]*)\s*\|([^|]+)\|(.+?)\s*\|\s*$", line)
            if m:
                index_map[m.group(1)] = (m.group(2).strip(), m.group(3).strip())

    # --- collect skills ----------------------------------------------
    cats = sorted(d for d in os.listdir(SRC) if re.match(r"^\d{2}-", d))
    skills = []  # (category, folder, src_dir, slug)
    used = {}
    for cat in cats:
        category = re.sub(r"^\d{2}-", "", cat)
        cpath = os.path.join(SRC, cat)
        for folder in sorted(os.listdir(cpath)):
            spath = os.path.join(cpath, folder)
            if not os.path.isdir(spath) or not os.path.isfile(os.path.join(spath, "SKILL.md")):
                continue
            slug = "cts-" + folder.lower().replace("_", "-")
            if slug in used:  # duplicate skill name across categories
                token = category.split("-")[0]
                slug = "cts-%s-%s" % (token, folder.lower().replace("_", "-"))
                if slug in used:
                    warn("could not dedupe %s/%s" % (cat, folder))
                print("DEDUPE: %s/%s -> %s (was %s)" % (cat, folder, slug, used.get(slug, "")))
            used[slug] = "%s/%s" % (cat, folder)
            skills.append((category, folder, spath, slug))

    print("skills found:", len(skills))

    # --- convert ------------------------------------------------------
    for variant, target in (("opencode", "OpenCode"), ("hermes", "Hermes")):
        count = 0
        for category, folder, spath, slug in skills:
            text, nl = read_text(os.path.join(spath, "SKILL.md"))
            m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            if m:
                fm_lines = m.group(1).splitlines()
                body = text[m.end():]
            else:
                fm_lines, body = [], text

            body, inline = process_body(body, slug, target, category)
            desc = extract_description(fm_lines) or inline
            if not desc:
                src, short = index_map.get(folder, ("?", "?"))
                desc = short if short != "?" else first_paragraph(body)
                warn("no description found for %s/%s - fallback used" % (category, folder))
            if not fm_lines and target == "hermes":
                pass  # fm_lines stays empty; head-only frontmatter is valid

            fm = build_frontmatter(fm_lines, slug, desc, target, category)
            dst = os.path.join(OUT, variant, category, slug)
            copy_skill(spath, dst)
            write_text(os.path.join(dst, "SKILL.md"), fm + body, nl)
            count += 1
        print("%s variant written: %d" % (variant, count))

    # --- README -------------------------------------------------------
    lines = [
        "# %s \u2014 Corporate Skill Pack" % BRAND,
        "",
        "> **%d skills** across **%d categories**, converted from"
        % (len(skills), len(cats)),
        "> [w95/awesome-claude-corporate-skills](https://github.com/w95/awesome-claude-corporate-skills) (MIT).",
        "> Built %s." % date.today().isoformat(),
        "",
        "## Variants",
        "",
        "| Variant | Layout | Status |",
        "|---------|--------|--------|",
        "| `opencode/` | `<category>/cts-<skill>/SKILL.md` | **Installed** to `~/.config/opencode/skills/` |",
        "| `hermes/` | `<category>/cts-<skill>/SKILL.md` | Staged only \u2014 copy into `~/.hermes/skills/` to activate |",
        "",
        "Skill IDs are identical in both variants (`cts-<original-name>`); duplicates across",
        "categories got the category as prefix (e.g. `cts-operations-vendor-management`).",
        "",
        "## License",
        "",
        "MIT (inherited from the source collection). Skills that ship their own",
        "`LICENSE`/`LICENSE.txt` file keep it \u2014 check those folders for details.",
        "",
        "## Skills by category",
        "",
    ]
    for cat in cats:
        category = re.sub(r"^\d{2}-", "", cat)
        members = [s for s in skills if s[0] == category]
        lines.append("### %s (%d)" % (category, len(members)))
        lines.append("")
        lines.append("| Skill ID | Source | Description |")
        lines.append("|----------|--------|-------------|")
        for _, folder, _, slug in members:
            src, desc = index_map.get(folder, ("\u2014", "\u2014"))
            desc = desc.replace("|", "\\|")
            lines.append("| `%s` | %s | %s |" % (slug, src, desc))
        lines.append("")
    write_text(os.path.join(OUT, "README.md"), "\n".join(lines), "\n")
    print("README.md written")

    # --- install OpenCode variant --------------------------------------
    if not os.path.isdir(OC_DEST):
        os.makedirs(OC_DEST)
    for entry in os.listdir(os.path.join(OUT, "opencode")):
        s = os.path.join(OUT, "opencode", entry)
        d = os.path.join(OC_DEST, entry)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    print("installed to", OC_DEST)

    if warnings:
        print("\n%d warning(s) - see above" % len(warnings))
    else:
        print("\nno warnings")


if __name__ == "__main__":
    main()
