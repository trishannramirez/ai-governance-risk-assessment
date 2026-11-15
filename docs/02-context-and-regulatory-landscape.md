# 02 – Context and Regulatory Landscape

> **Fictional organization.** Bluefin Health Analytics is invented for this portfolio project. It is the same company assessed in my [NIST CSF 2.0 Gap Assessment](https://github.com/trishannramirez/nist-csf-gap-analysis).
>
> **Not legal advice.** Regulatory status is summarized as of **November 2026** and changes often. Verify against primary sources.

## 1. Company context

Bluefin Health Analytics is a 220-person, Series C healthcare SaaS company. Its cloud platform helps about 140 US hospitals and clinic groups analyze patient flow, readmission risk, and staffing. It processes Protected Health Information (PHI) as a HIPAA **Business Associate**.

**Why an AI governance assessment now?**

1. **AI is already in the product.** ReadmitIQ (readmission risk prediction) influences which patients get follow-up care, and Support Copilot (a customer chatbot) launched in 2026.
2. **AI use inside the company has grown without oversight.** A staff survey found that **31% of employees** use personal AI accounts for work.
3. **EU expansion.** Bluefin signed a pilot with a hospital group in the Netherlands starting Q2 2027 and plans to hire 10 staff in Amsterdam. That brings Bluefin under the EU AI Act as a **provider** and a **deployer**.
4. **Customer pressure.** Hospital customers increasingly send AI due diligence questionnaires asking about model inputs, bias testing, and human oversight.
5. **The board asked** for an AI risk baseline after the cybersecurity assessment.

## 2. Scope

| In scope | Out of scope |
|---|---|
| All AI systems Bluefin builds, buys, or embeds (6 systems, see [03](03-ai-system-inventory-and-classification.md)) | Detailed technical model validation |
| Governance, policy, risk, and lifecycle practices | Customers' own AI systems |
| US and EU regulatory exposure | Jurisdictions other than the US and EU |

## 3. Frameworks used

| Framework | Type | How it is used here |
|---|---|---|
| **NIST AI RMF 1.0** (NIST AI 100-1) and **Generative AI Profile** (NIST AI 600-1) | Voluntary US framework | Maturity assessment of 19 categories across Govern, Map, Measure, Manage |
| **ISO/IEC 42001:2023** | Certifiable management system standard | Readiness assessment of Clauses 4–10 and Annex A control objectives |
| **EU AI Act** (Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744) | Binding EU law | Risk tier classification of each AI system |
| **OWASP Top 10 for LLM Applications (2025)** | Security reference | Threat mapping for generative AI risks |

NIST has said AI RMF 1.0 is being revised, but no revised text was published as of this assessment. Category IDs should be checked against any new version.

## 4. EU AI Act timeline (after the Digital Omnibus)

The Digital Omnibus on AI, Regulation (EU) 2026/1744, entered into force on 27 July 2026. It postponed the high-risk obligations but left the risk-based structure, prohibited practices, and transparency rules in place.

| Date | What applies | Relevance to Bluefin |
|---|---|---|
| 2 Feb 2025 | Prohibited practices (Art. 5); AI literacy (Art. 4) | Emotion recognition on employees (AI-05) is prohibited in the workplace; AI literacy measures needed for EU staff |
| 27 Jul 2026 | Omnibus in force. Art. 4 reworded to an obligation to **take measures to support** AI literacy, rather than guarantee a level | Training program still required |
| 2 Aug 2026 | Transparency obligations (Art. 50) | Support Copilot must disclose that users are interacting with AI (AI-02) |
| **2 Dec 2027** | High-risk obligations for **Annex III** systems | ATS candidate ranking for EU hires (AI-06) |
| **2 Aug 2028** | High-risk obligations for AI in **Annex I** regulated products (e.g., medical devices) | ReadmitIQ, *if* it qualifies as a medical device (AI-03) |

## 5. US considerations

| Requirement | Status (Nov 2026) | Relevance |
|---|---|---|
| **HIPAA** Privacy and Security Rules | In force | PHI in prompts (AI-01, AI-02); use of customer PHI to train ReadmitIQ (AI-03) must be allowed by BAAs or the data properly de-identified |
| **HHS Section 1557 rule, 45 CFR 92.210** (nondiscrimination in patient care decision support tools) | In the regulations since 2024, with obligations to identify and mitigate discrimination risk applicable from May 2025. Federal enforcement priorities have shifted since 2025, so confirm current status with counsel | Applies to Bluefin's **covered-entity customers**, who will ask Bluefin for information about ReadmitIQ's input variables and bias testing |
| **Colorado SB 26-189** (replaced the original Colorado AI Act, SB 24-205) | Signed 14 May 2026; effective 1 Jan 2027; narrower, notice-based framework for automated decision-making | May apply to AI-assisted hiring decisions for Colorado applicants (AI-06) |
| **NYC Local Law 144** | In force | Bias audit and notice requirements if the ATS ranking is used for NYC-based roles (AI-06) |
| **FDA clinical decision support software guidance** | Guidance | Determines whether ReadmitIQ could be regulated as a medical device in the US (AI-03) |

## Sources

- European Union, Regulation (EU) 2024/1689 (AI Act) and Regulation (EU) 2026/1744 (Digital Omnibus on AI)
- Gibson Dunn, *EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines and Other Key Changes* (2026)
- Cloud Security Alliance, *EU AI Act High-Risk Deadline Pushed to December 2027* (2026)
- Bristows, *The Digital Omnibus on AI: Key Changes to the EU AI Act* (2026)
- NIST, *AI Risk Management Framework* program page: https://www.nist.gov/itl/ai-risk-management-framework
- McDermott (mcdermottlaw.com), *Colorado AI bill signed after predecessor's enforcement blocked* (2026)
- HHS Office for Civil Rights, *Section 1557 Final Rule FAQs* and Dear Colleague letter on AI in patient care decision support tools
