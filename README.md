# CTSNexus

<img width="1024" height="572" alt="cts_nexus_banner" src="https://github.com/user-attachments/assets/15ffa69c-e940-4eb7-b130-5c6e1fc3d621" />

The CTS Nexus is a corporate skill pack featuring 166 skills across 14 categories, providing comprehensive support for various business, technological, and operational processes.

## Variants

| Variant | Layout | Status |
|---------|--------|--------|
| `opencode/` | `<category>/cts-<skill>/SKILL.md` | **Installed** to `~/.config/opencode/skills/` |
| `hermes/` | `<category>/cts-<skill>/SKILL.md` | Staged only — copy into `~/.hermes/skills/` to activate |

Skill IDs are identical in both variants (`cts-<original-name>`); duplicates across
categories got the category as prefix (e.g. `cts-operations-vendor-management`).

## License

MIT (inherited from the source collection). Skills that ship their own
`LICENSE`/`LICENSE.txt` file keep it — check those folders for details.

## Skills by category

### meta (1)

| Skill ID  | Description |
|----------|-------------|
| `cts-skill-creator` | Guidance for creating effective Harness Skills |

### executive-leadership (12)

| Skill ID | Description |
|----------|-------------|
| `cts-board-meeting-prep`  | Board decks, agendas, governance materials |
| `cts-change-management`  | Organizational change planning |
| `cts-competitive-analysis`  | Competitive landscape analysis |
| `cts-deep-research`  | Autonomous multi-step research using Gemini Deep Research Agent |
| `cts-executive-communication`  | All-hands, investor updates, crisis comms |
| `cts-internal-comms`  | Internal communications |
| `cts-knowledge-synthesis`  | Cross-source knowledge consolidation |
| `cts-kpi-dashboard`  | Executive scorecards, metric tracking |
| `cts-ma-due-diligence`  | M&A evaluation, integration planning |
| `cts-risk-assessment`  | Enterprise risk evaluation |
| `cts-strategic-planning`  | OKRs, SWOT, vision docs, strategic frameworks |
| `cts-task-management`  | Productivity and task tracking |

### finance-accounting (42)

| Skill ID | Description |
|----------|-------------|
| `cts-3-statements` | Three-statement financial models |
| `cts-buyer-list` | Potential buyer identification |
| `cts-catalyst-calendar` | Event catalyst tracking |
| `cts-check-model`  | Financial model auditing |
| `cts-cim-builder`  | Confidential Information Memorandums |
| `cts-client-report`  | Wealth management reports |
| `cts-client-review`  | Client portfolio reviews |
| `cts-comps-analysis`  | Comparable company analysis |
| `cts-datapack-builder`  | Data package assembly |
| `cts-dcf-model`  | Discounted cash flow valuation |
| `cts-dd-checklist`  | Due diligence checklists |
| `cts-dd-meeting-prep`  | DD meeting preparation |
| `cts-deal-screening`  | Deal evaluation criteria |
| `cts-deal-sourcing`  | Deal origination |
| `cts-deal-tracker`  | Deal pipeline management |
| `cts-earnings-analysis`  | Post-earnings analysis |
| `cts-earnings-preview`  | Pre-earnings estimates |
| `cts-financial-plan`  | Comprehensive financial planning |
| `cts-ic-memo`  | Investment committee memos |
| `cts-idea-generation`  | Investment idea generation |
| `cts-initiating-coverage`  | Research initiation reports |
| `cts-investment-proposal`  | Investment proposals |
| `cts-invoice-organizer`  | Invoice management |
| `cts-lbo-model`  | Leveraged buyout modeling |
| `cts-merger-model`  | Merger & acquisition modeling |
| `cts-model-update`  | Financial model updates |
| `cts-morning-note`  | Daily market briefings |
| `cts-pitch-deck`  | Investment banking pitch decks |
| `cts-portfolio-monitoring`  | Portfolio company tracking |
| `cts-portfolio-rebalance`  | Portfolio rebalancing |
| `cts-process-letter`  | M&A process letters |
| `cts-returns-analysis`  | Investment returns analysis |
| `cts-sector-overview`  | Industry sector reports |
| `cts-spglobal-earnings-preview` | S&P earnings previews |
| `cts-spglobal-funding-digest` | Funding round digests |
| `cts-spglobal-tear-sheet` | Company tear sheets |
| `cts-strip-profile`  | Financial strip profiles |
| `cts-tax-loss-harvesting`  | Tax-loss harvesting strategies |
| `cts-teaser`  | Deal teaser documents |
| `cts-thesis-tracker`  | Investment thesis monitoring |
| `cts-unit-economics`  | Unit economics analysis |
| `cts-value-creation-plan`  | PE value creation plans |

### human-resources (9)

| Skill ID  | Description |
|----------|-------------|
| `cts-compensation-benchmarking`  | Salary bands, pay equity |
| `cts-dei-strategy`  | Diversity & inclusion programs |
| `cts-employee-engagement-survey`  | Survey design & analysis |
| `cts-employee-handbook-builder`  | Policy handbooks |
| `cts-interview-kit-builder`  | Structured interview processes |
| `cts-job-description-writer`  | Inclusive, compelling JDs |
| `cts-onboarding-planner`  | 30-60-90 day onboarding plans |
| `cts-performance-review-assistant`  | Reviews, PIPs, feedback |
| `cts-resume-generator`  | Tailored resume creation |

### marketing (15)

| Skill ID  | Description |
|----------|-------------|
| `cts-brand-guidelines`  | Brand identity standards |
| `cts-brand-voice-enforcement`  | Voice consistency |
| `cts-campaign-planner`  | End-to-end campaign planning |
| `cts-canvas-design`  | Beautiful visual art in PNG/PDF with design philosophy |
| `cts-competitive-ads-extractor`  | Competitor ad analysis |
| `cts-content-research-writer`  | Research-driven content |
| `cts-discover-brand`  | Brand discovery |
| `cts-domain-name-brainstormer`  | Domain name ideation |
| `cts-email-marketing`  | Email campaigns & sequences |
| `cts-guideline-generation`  | Brand guideline creation |
| `cts-market-research`  | Market sizing, personas, trends |
| `cts-seo-content-optimizer`  | SEO optimization workflows |
| `cts-social-media-strategy`  | Multi-platform social strategy |
| `cts-theme-factory`  | Professional font & color themes for artifacts and reports |
| `cts-twitter-algorithm-optimizer`  | X/Twitter optimization |

### sales (16)

| Skill ID | Description |
|----------|-------------|
| `cts-account-research`  | Account intelligence |
| `cts-account-research-common-room`  | Account signals |
| `cts-call-prep`  | Sales call preparation |
| `cts-call-prep-common-room`  | Signal-based call prep |
| `cts-competitive-intelligence`  | Competitive battlecards |
| `cts-compose-outreach`  | Outreach composition |
| `cts-contact-research`  | Contact intelligence |
| `cts-create-an-asset`  | Sales collateral creation |
| `cts-daily-briefing`  | Daily sales briefings |
| `cts-draft-outreach`  | Outreach email drafting |
| `cts-enrich-lead` | Apollo | Lead enrichment |
| `cts-lead-research-assistant`  | Lead qualification |
| `cts-prospect-apollo` | Apollo | Prospecting via Apollo |
| `cts-prospect-common-room`  | Signal-based prospecting |
| `cts-sequence-load` | Apollo | Outreach sequences |
| `cts-weekly-prep-brief`  | Weekly prep briefs |

### legal-compliance (7)

| Skill ID | Description |
|----------|-------------|
| `cts-canned-responses`  | Standard legal responses |
| `cts-compliance`  | Regulatory compliance |
| `cts-compliance-tracking`  | Compliance monitoring |
| `cts-contract-review`  | Clause-by-clause review |
| `cts-legal-risk-assessment`  | Legal risk evaluation |
| `cts-meeting-briefing`  | Legal meeting prep |
| `cts-nda-triage`  | NDA automated triage |

### operations (11)

| Skill ID | Description |
|----------|-------------|
| `cts-business-case-builder`  | ROI and business cases |
| `cts-file-organizer`  | File organization |
| `cts-incident-postmortem`  | Blameless postmortems |
| `cts-kaizen`  | Continuous improvement using Japanese Kaizen & Lean methodology |
| `cts-meeting-insights-analyzer` | Meeting analysis |
| `cts-memory-management`  | Context management |
| `cts-process-optimization` | Process improvement |
| `cts-project-status-report` | RAG status reports |
| `cts-resource-planning` | Resource allocation |
| `cts-sop-builder` | Standard Operating Procedures |
| `cts-vendor-management` | Vendor relationships |

### it-engineering (14)

| Skill ID | Description |
|----------|-------------|
| `cts-changelog-generator` | Release changelogs |
| `cts-code-review`  | Code review workflows |
| `cts-developer-growth-analysis`  | Dev metrics |
| `cts-documentation`  | Technical documentation |
| `cts-frontend-design`  | Frontend UI design |
| `cts-incident-response`  | Incident management |
| `cts-langsmith-fetch`  | LangSmith integration |
| `cts-mcp-builder`  | MCP server creation |
| `cts-software-architecture`  | Clean Architecture, SOLID, and design patterns |
| `cts-system-design`  | Architecture design |
| `cts-tech-debt`  | Technical debt management |
| `cts-test-driven-development`  | TDD methodology for features and bugfixes |
| `cts-testing-strategy`  | Test planning |
| `cts-webapp-testing`  | Web app testing |

### product-management (10)

| Skill ID | Description |
|----------|-------------|
| `cts-brainstorming`  | Transform rough ideas into fully-formed designs |
| `cts-doc-coauthoring`  | Collaborative writing |
| `cts-feature-spec`  | Feature specifications |
| `cts-prd-writer`  | Product requirements docs |
| `cts-product-launch-playbook`  | Launch planning |
| `cts-roadmap-builder`  | Product roadmaps |
| `cts-search-strategy`  | Information search |
| `cts-source-management`  | Source tracking |
| `cts-sprint-planning`  | Agile sprint planning |
| `cts-user-research-synthesizer`  | Research synthesis |

### data-analytics (9)

| Skill ID | Description |
|----------|-------------|
| `cts-csv-data-summarizer`  | Auto-analyze CSV files with insights & visualizations |
| `cts-data-context-extractor`  | Data context extraction |
| `cts-data-exploration`  | Exploratory data analysis |
| `cts-data-validation`  | Data quality checks |
| `cts-data-visualization`  | Charts & visualizations |
| `cts-interactive-dashboard-builder`  | Dashboard creation |
| `cts-postgres`  | Safe read-only PostgreSQL queries with multi-connection support |
| `cts-sql-queries`  | SQL query generation |
| `cts-statistical-analysis`  | Statistical methods |

### customer-success (10)

| Skill ID | Description |
|----------|-------------|
| `cts-churn-analysis`  | Churn prediction & retention |
| `cts-customer-research`  | Customer intelligence |
| `cts-escalation`  | Escalation management |
| `cts-knowledge-management`  | Knowledge base management |
| `cts-onboarding-playbook`  | Customer onboarding |
| `cts-qbr-builder`  | Quarterly Business Reviews |
| `cts-response-drafting`  | Response templates |
| `cts-slack-messaging`  | Slack communication |
| `cts-slack-search`  | Slack search |
| `cts-ticket-triage`  | Support ticket routing |

### procurement-supply-chain (6)

| Skill ID | Description |
|----------|-------------|
| `cts-contract-negotiation`  | Negotiation prep |
| `cts-inventory-forecasting`  | Demand forecasting |
| `cts-rfp-builder`  | Request for Proposals |
| `cts-supplier-scorecard`  | Supplier performance |
| `cts-vendor-evaluation`  | Vendor comparison |
| `cts-procurement-vendor-management`  | Vendor relationships |

### document-processing (4)

| Skill ID | Description |
|----------|-------------|
| `cts-docx`  | Create, edit, analyze Word docs with tracked changes, comments, formatting |
| `cts-pdf`  | Extract text, tables, metadata, merge & annotate PDFs |
| `cts-pptx`  | Read, generate, and adjust slides, layouts, templates |
| `cts-xlsx`  | Spreadsheet manipulation: formulas, charts, data transformations |
