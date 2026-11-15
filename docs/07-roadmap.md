# 07 – AI Governance Roadmap

The roadmap sequences the risk treatments in [06](06-ai-risk-register.md) and the NIST AI RMF and ISO/IEC 42001 recommendations around **regulatory deadlines** and the **Netherlands pilot (Q2 2027)**.

## Phase 1: Stop the bleeding (by 31 January 2027)

| Action | Risks | Owner | Deadline driver |
|---|---|---|---|
| Disable voice-based emotion analysis in the sales call platform | R16 | CFO | EU AI Act Art. 5(1)(f); Amsterdam hires in 2027 |
| Approve the [AI Acceptable Use Policy](../policies/ai-acceptable-use-policy.md); publish the approved AI tools list | R01, R02 | CISO / GRC | 31% shadow AI usage |
| Block unapproved AI services at the secure web gateway; roll out Bluefin Assist to all staff | R02 | CISO | |
| Charter the AI Governance Committee; assign an owner to every AI system | R18 | CISO | |
| Require the [AI Use Case Intake Form](../templates/ai-use-case-intake-form.md) for all new AI | R14, R18 | GRC | StaffSense roadmap decision |
| Add AI disclosure to Support Copilot | R05 | VP Customer Success | Art. 50(1), in force since 2 Aug 2026 |
| Legal review of training data rights in all 12 BAAs; document de-identification | R09 | General Counsel | Before any further training |

## Phase 2: Build the foundations (February to April 2027)

| Action | Risks | Owner |
|---|---|---|
| Written regulatory determination for ReadmitIQ (EU MDR and FDA); limit pilot scope until resolved | R11 | General Counsel |
| ReadmitIQ bias testing by race and ethnicity, sex, age, and payer; review proxy variables | R07 | VP Product |
| ReadmitIQ performance and drift monitoring; local validation before the Netherlands go-live | R08 | Data Science Lead |
| Publish the ReadmitIQ model facts sheet for customers | R12 | VP Product |
| Show top contributing factors and human oversight guidance in the ReadmitIQ UI | R10 | VP Product |
| Red-team Support Copilot; tenant-scoped retrieval; output filtering; confirmation before ticket actions | R03, R04 | CTO |
| Pin LLM model versions; build the regression test set; rate limits and spend alerts | R06, R21 | CTO |
| Add AI questions to vendor due diligence; no-training clauses; review SaaS AI settings | R15 | GRC / Procurement |
| Launch role-based AI literacy training | R19 | HR / CISO |
| DLP scanning for PHI in Bluefin Assist prompts | R01 | CTO |

## Phase 3: Operate and certify (May 2027 onward)

| Action | Risks / Framework | Owner |
|---|---|---|
| AI incident playbooks in the IR plan; AI tabletop exercise | R20; MANAGE 4 | Security Ops |
| ATS: vendor bias audit, human review of rejections, candidate notices | R17; Art. 26 by 2 Dec 2027 | VP People |
| Rate limiting and anomaly alerts on the ReadmitIQ scoring API | R13 | CISO |
| AI impact assessments for ReadmitIQ, ATS, and Support Copilot | MAP 5; ISO A.5 | GRC / Privacy |
| Quarterly AI risk review; annual AI RMF re-assessment | MANAGE 1; ISO Clause 9 | GRC |
| ISO/IEC 42001 internal audit and management review; Stage 1 certification audit | ISO Clauses 9–10 | GRC |
| If ReadmitIQ is high-risk: technical documentation, quality management, and conformity assessment ahead of 2 Aug 2028 | Arts. 9–17, 43 | VP Product / Legal |

## Key dates

| Date | Milestone |
|---|---|
| 31 Dec 2026 | Emotion recognition feature disabled |
| 1 Jan 2027 | Colorado SB 26-189 takes effect |
| 31 Jan 2027 | Phase 1 complete |
| Q2 2027 | Netherlands pilot begins (requires R05, R08, R11 resolved) |
| 2 Dec 2027 | EU AI Act Annex III obligations (ATS) |
| 2 Aug 2028 | EU AI Act Annex I obligations (ReadmitIQ, if a medical device) |

## Success metrics

| KPI | Baseline | Target (12 months) |
|---|---|---|
| AI systems with a named owner and inventory record | 0 of 6 (before this assessment) | 100% |
| Staff using unapproved AI tools | 31% | < 5% |
| Critical AI risks | 5 | 0 |
| NIST AI RMF average maturity | 1.16 | 2.95 |
| ISO/IEC 42001 average readiness | 0.94 | 3.00 |
| AI literacy training completion | 0% | 95% |
| ReadmitIQ subgroup performance reviews | 1 (2024) | Quarterly |
