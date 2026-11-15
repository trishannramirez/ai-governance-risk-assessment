# AI Acceptable Use Policy

| | |
|---|---|
| **Organization** | Bluefin Health Analytics, Inc. (fictional) |
| **Policy owner** | Chief Information Security Officer |
| **Approved by** | AI Governance Committee *(draft for approval)* |
| **Version** | 1.0 (draft) |
| **Effective date** | 1 January 2027 |
| **Review cycle** | Every 6 months, or sooner if laws or tools change significantly |
| **Related policies** | Information Security Policy, Data Classification Policy, HIPAA Privacy and Security Policies, Vendor Risk Management Policy, Incident Response Plan |
| **Framework alignment** | NIST AI RMF GOVERN 1; ISO/IEC 42001 A.2, A.9; EU AI Act Art. 4 and Art. 5 |

---

## 1. Purpose

AI tools can make our work faster and better. They also create new risks: exposing patient data, producing wrong information, and making unfair decisions. This policy explains how Bluefin employees may use AI tools safely, legally, and in line with our commitments to customers and patients.

## 2. Scope

This policy applies to:
- all employees, contractors, and interns (**"workforce members"**)
- all AI tools used for Bluefin work, whether provided by Bluefin, built into other software, or accessed personally
- all AI features Bluefin builds into its products

**"AI tool"** means any software that generates text, code, images, audio, or video, or makes predictions or recommendations using machine learning. Examples include chat assistants, coding assistants, meeting note-takers, and AI features inside SaaS products.

## 3. Core principles

1. **Protect patient and customer data.** Patient trust is the foundation of our business.
2. **You are responsible for your output.** AI assists you; it does not replace your judgment. You own everything you submit, send, or ship, whether or not AI helped.
3. **Be transparent.** Don't present AI output as human work where that matters, and always tell people when they are interacting with AI.
4. **Use approved tools only.** If a tool isn't approved, ask before using it.
5. **When in doubt, ask.** Contact the GRC team at *#ai-governance*.

## 4. Approved AI tools

The **Approved AI Tools List** is maintained by the GRC team on the intranet. Approved tools have passed security, privacy, and legal review, and have contracts that prevent the vendor from training on our data.

| Data classification | Approved tools allowed? | Notes |
|---|---|---|
| **Public** | ✅ Yes | |
| **Internal** | ✅ Yes | |
| **Confidential** (customer data, source code, financials) | ✅ Only tools marked "Confidential OK" | |
| **Restricted** (PHI, credentials, secrets) | ⚠️ Only tools marked "PHI approved" and only for an approved use case | Bluefin Assist is the only tool currently covered by a BAA |

**Personal AI accounts** (free or paid consumer accounts) **must never be used for Bluefin work**, with any data classification above Public.

## 5. Prohibited uses

Workforce members must **not**:

1. Enter **PHI, credentials, API keys, or secrets** into any AI tool not explicitly approved for that data.
2. Use AI tools that are **not on the Approved AI Tools List** for Bluefin work.
3. Use AI to make or materially influence **decisions about individuals** (hiring, firing, promotion, performance, or patient care) without a documented human review and an approved use case.
4. Use AI to **infer emotions** of employees or job candidates, or to categorize people by sensitive traits (race, health, religion, sexual orientation, political views) from biometric data.
5. Present AI-generated content to customers, regulators, or auditors as verified fact **without human review**, especially security, compliance, contractual, or clinical statements.
6. Use AI to generate content that impersonates real people, or that is deceptive, discriminatory, or harassing.
7. Enable **AI features in existing SaaS tools** (e.g., note-takers, auto-summarization) without IT approval.
8. Use AI meeting recorders or note-takers on **customer calls** without the approval of the call owner and the consent of all participants.
9. Build, buy, or launch any new AI system or feature without submitting the [AI Use Case Intake Form](../templates/ai-use-case-intake-form.md).

## 6. Requirements when using AI

### 6.1 Review and verify
- Check AI output for accuracy before using it. AI can produce confident but wrong answers.
- Verify citations, statistics, legal or regulatory statements, and code before relying on them.
- Run all AI-generated code through normal code review, security scanning, and testing.

### 6.2 Protect data
- Remove or de-identify customer and patient information before prompting, unless the tool is approved for that data.
- Do not upload customer files to AI tools unless the tool is approved for Confidential data.

### 6.3 Respect intellectual property
- Don't enter third-party confidential information you are not authorized to share.
- Check the license of AI-generated code suggestions before using them in Bluefin products.

### 6.4 Be transparent
- Customer-facing AI (such as Support Copilot) must clearly tell users they are interacting with AI.
- Disclose substantial AI assistance where the reader would reasonably expect to know (for example, in reports to customers or regulators).

## 7. AI in Bluefin products

All AI features in Bluefin products must:
1. Go through the AI Use Case Intake Form and be classified by risk and regulatory status **before** development starts.
2. Have a named **AI system owner** recorded in the AI inventory.
3. Meet the release criteria set by the AI Governance Committee, including evaluation, bias testing (for features that affect people), and security testing.
4. Be monitored in production, with a documented way to disable or roll back.
5. Have customer-facing documentation of intended use, limitations, and human oversight expectations.

## 8. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| **All workforce members** | Follow this policy; complete AI literacy training; report misuse or problems |
| **Managers** | Make sure their teams understand and follow the policy |
| **AI Governance Committee** | Approves high-risk use cases, release criteria, and policy changes; reviews AI risks quarterly |
| **GRC team** | Maintains the Approved AI Tools List, the AI inventory, and the risk register; reviews intake forms |
| **IT and Security** | Enforces technical controls (blocking unapproved tools, DLP); reviews SaaS AI settings |
| **AI system owners** | Accountable for the risk, monitoring, and documentation of their AI system |

## 9. Training

All workforce members must complete **AI literacy training** within 30 days of hire and once a year after that. Engineers, data scientists, support agents, and recruiters complete additional role-based modules.

## 10. Reporting and incidents

Report the following immediately to *#security-incidents* or security@bluefin.example:
- PHI or confidential data entered into an unapproved AI tool
- AI output that was harmful, biased, or clearly wrong and reached a customer or patient
- Suspected manipulation of a Bluefin AI system (for example, prompt injection)

Reports made in good faith will not result in retaliation. Prompt self-reporting of accidental misuse is treated as a mitigating factor.

## 11. Exceptions

Exceptions require a written request to the GRC team, a risk assessment, and approval by the CISO. Approved exceptions are time-limited (maximum 12 months) and recorded in the risk register.

## 12. Enforcement

Violations may lead to removal of tool access and disciplinary action, up to and including termination. Violations involving PHI are also handled under the HIPAA sanctions policy.

## 13. Definitions

| Term | Definition |
|---|---|
| **AI system** | A machine-based system that infers from inputs how to generate outputs such as predictions, content, recommendations, or decisions |
| **Generative AI** | AI that produces new content (text, code, images, audio, video) |
| **PHI** | Protected Health Information as defined by HIPAA |
| **Shadow AI** | Use of AI tools that are not approved by Bluefin |
| **Prompt** | Text or files given to an AI tool as input |
| **Human review** | A qualified person checks the AI output and can change or reject it before it is used |

---

*Document history: v1.0 draft, November 2026, prepared as part of the AI Governance Risk Assessment.*
