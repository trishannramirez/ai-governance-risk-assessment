# 03 – AI System Inventory and EU AI Act Classification

Before this assessment, Bluefin had no AI inventory. The inventory below was built from interviews with Product, Engineering, Data Science, People, and Finance, a review of SaaS admin consoles, and a staff survey. The full record, with data, owners, and regulatory notes, is in [`data/ai_system_inventory.csv`](../data/ai_system_inventory.csv).

## Inventory summary

| ID | System | What it does | Built or bought | Bluefin's EU role | PHI | Inherent risk |
|---|---|---|---|---|---|---|
| AI-01 | **Bluefin Assist** | Internal generative AI assistant for drafting, summarizing, coding | Bought (enterprise LLM through cloud provider) | Deployer | Possible | High |
| AI-02 | **Support Copilot** | Customer support chatbot with retrieval over help articles; can open and update tickets | Built on a third-party general-purpose model | Provider | Possible | High |
| AI-03 | **ReadmitIQ** | Predicts 30-day readmission risk for each patient to prioritize care-manager outreach | Built in-house | Provider | **Yes** | **Critical** |
| AI-04 | **StaffSense** | Forecasts patient volume per unit for staffing levels (aggregate only) | Built in-house | Provider | No | Medium |
| AI-05 | **Vendor AI features** | Meeting note-taker, AI coding assistant, sales call intelligence with voice emotion analysis | Bought | Deployer | Possible | High |
| AI-06 | **ATS candidate ranking** | Scores and ranks job applicants | Bought | Deployer | No | High |

## EU AI Act classification

The classification follows the Act's four-step logic: (1) Is it an AI system? (2) Is it a prohibited practice (Art. 5)? (3) Is it high-risk under Annex I (regulated products) or Annex III (listed use cases)? (4) Do transparency obligations apply (Art. 50)? If none of these, it is minimal risk.

| ID | System | Prohibited? | High-risk? | Transparency (Art. 50)? | **Tier** | Applies from |
|---|---|---|---|---|---|---|
| AI-01 | Bluefin Assist | No | No | No (internal use, no generated content published) | **Minimal** (Art. 4 literacy applies) | 2 Feb 2025 |
| AI-02 | Support Copilot | No | No | **Yes**: users interact directly with AI (Art. 50(1)) | **Limited (transparency)** | 2 Aug 2026 |
| AI-03 | ReadmitIQ | No | **Likely, via Annex I** if it qualifies as medical device software under EU MDR | No | **Likely high-risk, pending determination** | 2 Aug 2028 |
| AI-04 | StaffSense | No | No (aggregate forecasts only) | No | **Minimal**; becomes high-risk if extended to individual workers | — |
| AI-05 | Vendor AI features | **Yes, for one feature**: voice-based emotion recognition on employees (Art. 5(1)(f)) | No | No | **Prohibited feature** must be disabled; otherwise minimal | 2 Feb 2025 |
| AI-06 | ATS candidate ranking | No | **Yes**: recruitment and selection (Annex III(4)(a)) | No | **High-risk (Bluefin as deployer)** | 2 Dec 2027 |

## Rationale for the harder calls

### AI-03 ReadmitIQ: likely high-risk, pending a regulatory determination
ReadmitIQ produces patient-level risk scores that influence which patients receive follow-up care. Under EU MDR, software whose intended purpose is to provide information used to make decisions for diagnostic or therapeutic purposes can qualify as a medical device. If ReadmitIQ requires notified-body conformity assessment under MDR, it is a high-risk AI system under **Art. 6(1) and Annex I**, and provider obligations (risk management, data governance, technical documentation, human oversight, accuracy and robustness, post-market monitoring) apply from **2 August 2028**.

Bluefin's 2024 product spec describes the intended purpose as "prioritizing care management outreach," which could support an argument that it is not a medical device. That wording was written without regulatory input. **This determination needs regulatory counsel before the Netherlands pilot starts** (risk R11).

Even if ReadmitIQ is ultimately not high-risk, the recommended controls (bias testing, monitoring, documentation, human oversight) are justified by patient-safety risk and customer due diligence.

### AI-05 Vendor AI features: a prohibited practice hiding in a sales tool
The sales call-intelligence platform includes a feature that infers emotions from callers' voices, and it is enabled for Bluefin's own sales reps. Inferring emotions of people in the workplace from biometric data such as voice is prohibited under **Art. 5(1)(f)** (with narrow medical and safety exceptions). Once Bluefin hires sales staff in Amsterdam, this feature must be off. The simplest fix is to disable it for all users (risk R16, target **31 Dec 2026**).

### AI-04 StaffSense: minimal today, high-risk if the roadmap is not controlled
StaffSense forecasts aggregate patient volume and makes no decisions about individual workers. A 2027 roadmap item would recommend shift assignments for individual nurses. That would fall under **Annex III(4)(b)** (allocating tasks based on individual behavior or traits) for EU customers. The control is a classification gate at roadmap approval, not a technical fix (risk R14).

### AI-06 ATS candidate ranking: Bluefin is a deployer of a high-risk system
Bluefin did not build the ranking feature, but as the **deployer** it will have obligations under **Art. 26** from 2 December 2027 for EU candidates. These include using the system according to the provider's instructions, assigning trained human oversight, monitoring operation, keeping logs, and informing affected people. Candidates may also have a right to an explanation (**Art. 86**). US hiring laws (Colorado SB 26-189, NYC Local Law 144, Title VII) add parallel obligations.

## Provider vs. deployer summary

| Role | Systems | Main obligations |
|---|---|---|
| **Provider** (Bluefin builds and places on the market) | AI-02, AI-03, AI-04 | Transparency by design (AI-02); full high-risk provider obligations if ReadmitIQ is confirmed high-risk (AI-03) |
| **Deployer** (Bluefin uses under its authority) | AI-01, AI-05, AI-06 | AI literacy; do not use prohibited features; Art. 26 duties for the high-risk ATS |
