# Tracking YoY AI Adoption & Developer Sentiment (2024–2025)

## 🔄 Project Phase: 1. ASK
This portfolio project analyzes the shifting dynamics between software engineers and Artificial Intelligence productivity tools using microdata from the 2024 and 2025 Stack Overflow Developer Surveys.

### 🏢 The Business Objective & Problem Statement
In the wake of rapid corporate investments into AI coding tools, engineering leaders and tech companies need data-driven answers to a critical question: Is real-world productivity matching the marketing hype, or are developers facing tool fatigue and trust friction? 

By analyzing year-over-year (YoY) microdata, this project aims to provide actionable insights for technical leaders to guide their team tooling and procurement strategies.

### 👥 Key Stakeholders
* **Engineering Directors / CTOs:** Need to know if AI tools actually support their workforce or create technical debt.
* **Product Managers (AI Tools):** Need to identify where friction points (trust, usability) are occurring in the dev ecosystem.
* **Recruiters / Talent Teams:** Evaluating my ability to handle complex, real-world data pipelines and translate them into business strategy.

### ❓ Key Analytical Questions
1. **Adoption Scale:** How did overall AI tool adoption rates change among developers from 2024 to 2025?
2. **The Sentiment Paradox:** Did developer trust and sentiment toward these tools improve, plateau, or decline year-over-year?
3. **Experience Segmentation:** Do these trends differ significantly when comparing junior developers against seasoned senior engineers?


## 📁 Project Phase: 2. PREPARE

### Data Sources & Integrity
* **Source:** Stack Overflow Developer Survey Microdata (2024 & 2025 public archives).
* **Format:** Local flat `.csv` files stored in partitioned directories (`data/raw_2024/`, `data/raw_2025/`).
* **Storage Strategy:** Maintained locally to establish an infrastructure-lean baseline before considering cloud migration.

### Variable Schema Mapping
To ensure longitudinal consistency, the following schema mapping boundaries have been established:
1. **Experience Segment:** Derived from `YearsCodePro`.
   * *Junior Cohort:* $\le$ 3 Years Professional Experience
   * *Senior Cohort:* $\ge$ 8 Years Professional Experience
2. **AI Tool Adoption:** Tracked via `AISelect` (Binary: Yes/No context).
3. **AI Trust Metrics:** Tracked via `AITrust` (Ordinal scale assessing automated tool output reliability).