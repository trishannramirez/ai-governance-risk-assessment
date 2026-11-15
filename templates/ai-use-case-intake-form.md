# AI Use Case Intake Form

Complete this form **before** building, buying, or enabling any AI system or AI feature at Bluefin Health Analytics (fictional). The GRC team reviews submissions within 5 business days. High-risk use cases go to the AI Governance Committee.

*Framework alignment: NIST AI RMF MAP 1–5; ISO/IEC 42001 Clause 6.1.4 and A.5; EU AI Act Arts. 5, 6, and 50*

---

## Section 1: Basic information

| Field | Response |
|---|---|
| Use case name | |
| Requester (name, team) | |
| Proposed AI system owner | |
| Target launch date | |
| Build, buy, or enable an existing vendor feature? | ☐ Build ☐ Buy ☐ Vendor feature |
| Vendor and model (if applicable) | |

## Section 2: Purpose and context (MAP 1, MAP 3)

1. What problem does this solve, and what is the expected benefit?
2. Who will use the system? (internal staff / customer staff / patients / public)
3. Who is affected by its outputs, even if they don't use it directly?
4. What does it produce? ☐ Content ☐ Prediction or score ☐ Recommendation ☐ Automated decision ☐ Action in another system
5. Is a human reviewing every output before it takes effect? ☐ Yes ☐ No ☐ Sometimes. Explain:
6. What is explicitly **out of scope** (uses the system must not be used for)?
7. What happens today without AI? (baseline for comparison)

## Section 3: Data (MAP 4, ISO A.7)

| Question | Response |
|---|---|
| Highest data classification processed | ☐ Public ☐ Internal ☐ Confidential ☐ Restricted (PHI) |
| Will PHI be used for **training**, **input**, or **output**? | |
| Data sources and our right to use them (BAA, contract, consent, de-identified) | |
| Does any input measure race, ethnicity, sex, age, disability, or national origin, or likely act as a proxy for them? | ☐ Yes ☐ No ☐ Unsure |
| Will the vendor store prompts or data, or use them for training? | |
| Where is data processed (regions)? | |

## Section 4: EU AI Act screening (GRC completes with requester)

**Step 1: Prohibited practices (Art. 5).** Does the system do any of the following? If yes, **stop**: the use case cannot proceed.
- ☐ Infer emotions of people at work or in education (except for medical or safety reasons)
- ☐ Categorize people by sensitive traits based on biometric data
- ☐ Social scoring, or manipulative or deceptive techniques that cause significant harm
- ☐ Exploit vulnerabilities due to age, disability, or social or economic situation
- ☐ Untargeted scraping of facial images, or real-time remote biometric identification

**Step 2: High-risk (Art. 6).**
- ☐ Is it, or is it a safety component of, a product regulated under Annex I (e.g., **medical device software**)?
- ☐ Is it used in an Annex III area: **employment** (recruiting, promotion, task allocation, monitoring), access to essential services, education, critical infrastructure, biometrics, law enforcement, migration, or justice?

**Step 3: Transparency (Art. 50).**
- ☐ Do people interact with it directly (e.g., a chatbot)?
- ☐ Does it generate synthetic audio, images, video, or text published to inform the public?

**Step 4: Bluefin's role.** ☐ Provider (we build or brand it) ☐ Deployer (we use it)

## Section 5: US and sector considerations

- ☐ Could it be clinical decision support or a medical device (FDA)?
- ☐ Does it support patient care decisions that our covered-entity customers must assess under HHS Section 1557?
- ☐ Is it used in hiring or other employment decisions (state and city AI hiring laws, Title VII)?
- ☐ Does it involve recording calls or meetings (consent laws)?

## Section 6: Risk screening (MAP 5, MEASURE 2)

Rate each from 1 (low) to 5 (high):

| Risk area | Rating | Notes |
|---|---|---|
| Harm to patients if the output is wrong | | |
| Unfair impact on particular groups | | |
| Privacy or data exposure | | |
| Security (prompt injection, data leakage, model abuse) | | |
| Reliability (hallucination, drift) | | |
| Legal and regulatory exposure | | |
| Reputational impact | | |

## Section 7: Controls planned

- ☐ Human review before outputs take effect
- ☐ Evaluation test set and acceptance thresholds
- ☐ Bias testing across relevant groups
- ☐ Security testing / red teaming (OWASP Top 10 for LLM Applications)
- ☐ Production monitoring and alerts
- ☐ Kill switch or rollback
- ☐ User-facing disclosure and documentation of limitations
- ☐ Vendor contract: no training on our data, retention limits, BAA if PHI

## Section 8: Decision (GRC / AI Governance Committee)

| Field | Response |
|---|---|
| Risk tier | ☐ Low ☐ Medium ☐ High ☐ Prohibited |
| EU AI Act tier | ☐ Minimal ☐ Transparency ☐ High-risk ☐ Prohibited |
| Impact assessment required? | ☐ Yes ☐ No |
| Decision | ☐ Approved ☐ Approved with conditions ☐ Rejected |
| Conditions | |
| Approver and date | |
| Added to AI inventory as | AI-__ |
| Review date | |
