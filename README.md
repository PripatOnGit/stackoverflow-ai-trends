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


## 🔄 Project Phase: 3. PROCESS & 4. ANALYZE

### 🗄️ SQL Data Transformation & Aggregation
To extract data-driven insights across historical periods, the raw 2024 and 2025 microdata tables were compiled into a centralized tracking table (`raw_survey_data`). Window functions (`PARTITION BY`) were applied to handle shifting denominator sizes across survey years.

#### Query 1: Overall YoY AI Tool Adoption Rate
```sql
SELECT 
    survey_year,
    "AISelect" AS ai_use_status,
    COUNT(*) AS developer_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY survey_year), 2) AS percentage
FROM raw_survey_data
WHERE "AISelect" IS NOT NULL
GROUP BY survey_year, "AISelect"
ORDER BY survey_year ASC, percentage DESC;```

####Query 2: YoY Shift in Developer Sentiment / Trust
```sql
SELECT 
    survey_year,
    "AISent" AS ai_sentiment,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY survey_year), 2) AS percentage
FROM raw_survey_data
WHERE "AISent" IS NOT NULL
GROUP BY survey_year, "AISent"
ORDER BY survey_year ASC, percentage DESC;```

###Query 3: Experience Level Breakdown (Junior vs Senior)
 ```sql
SELECT 
    survey_year,
    CASE WHEN "YearsCodePro" <= 3 THEN 'Junior (<=3 yrs exp)'
         ELSE 'Senior (>3 yrs exp)' END AS experience_tier,
    "AISelect" AS ai_use_status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY survey_year, CASE WHEN "YearsCodePro" <= 3 THEN 'Junior (<=3 yrs exp)' ELSE 'Senior (>3 yrs exp)' END), 2) AS percentage
FROM raw_survey_data
WHERE "YearsCodePro" IS NOT NULL AND "AISelect" IS NOT NULL
GROUP BY survey_year, experience_tier, "AISelect"
ORDER BY survey_year ASC, experience_tier ASC, percentage DESC;```


### 🔄 Project Phase: 5. SHARE (Data Visualizations)

### 📈 Executive Data Storytelling
The following visualizations illustrate the macro shifts in developer behavior over the last two years, highlighting the definitive transition from experimental tool-testing to normalized production workflows.
Chart 1: AI Tool Adoption Rates (YoY)X-Axis: Year (2024 vs. 2025)Y-Axis: Percentage (0% to 100%)Series/Legend: Yes (Adopting), No, but planning to, No, and not planning toWhat it reveals: The visual shrinking of the "No" buckets and the expanding "Yes" block.

Chart 2: Developer Trust Maturity Curve (YoY)X-Axis: Sentiment Categories (Highly Trust, Somewhat Trust, Neither Trust nor Distrust, etc.)Y-Axis: PercentageSeries/Legend: Color-coded by Year (2024 vs. 2025)What it reveals: A clear visual plateau showing that despite massive adoption, developers are moving into the pragmatic "Neither Trust nor Distrust" middle ground.

Chart 3: Experience Cohort Variance Layout: Two side-by-side grouped charts—one for Junior ($\le 3$ years) and one for Senior ($>3$ years).What it reveals: Highlights the "Junior Guidance Gap," showing that the "Yes" adoption line peaks significantly higher for less experienced engineers.📂 Updating Your Repository with Visuals

#Tableau Notebook Link: https://public.tableau.com/app/profile/priyanka.patil2211/viz/AIAdoptionTrends2024-2025/AIAdoptionTrends2024-2025?showOnboarding=true


🏢 Business Background & Problem Statement
Over the last two years, organizations have aggressively invested capital into enterprise AI coding assistants (e.g., GitHub Copilot, Gemini Code Assist). Tech executives face a critical question: Are engineering teams actually embracing these tools, or are we experiencing tool friction and platform fatigue? >
This analysis leverages microdata from the Stack Overflow Developer Surveys (2024–2025) to evaluate macro trends in developer adoption, sentiment shifts, and experience-based variance.

🏢 Executive Report: Navigating the AI Hype Cycle in Engineering Teams
Business Background & Problem Statement
Over the last two years, organizations have aggressively invested capital into enterprise AI coding assistants (e.g., GitHub Copilot, Gemini Code Assist). Tech executives face a critical question: Are engineering teams actually embracing these tools, or are we experiencing tool friction and platform fatigue?

This analysis leverages microdata from the Stack Overflow Developer Surveys (2024–2025) to evaluate macro trends in developer adoption, sentiment shifts, and experience-based variance.

💡 Key Data-Driven Insights
Insight 1: AI Tools are No Longer Optional. YoY data shows overall developer adoption climbed past the two-thirds threshold by 2025. The "Wait and See" cohort dropped significantly, confirming that workflows are permanently modernizing.

Insight 2: Pragmatic Skepticism Trumps Blind Trust. Despite soaring adoption rates, developer sentiment indicates a clear maturity curve. The majority of developers maintain a "trust but verify" stance, meaning engineering leaders cannot expect AI to replace thorough code-review processes.

Insight 3: The Junior Guidance Gap. Junior engineers adopt and rely on AI tools significantly faster than seniors. While this accelerates initial velocity, it introduces a business risk regarding code quality and architectural foundations if left unmonitored by senior oversight.

🚀 Strategic Recommendations for Leadership
Establish Guardrails for Junior Staff: Create structured internal guidelines on how junior engineers use AI tools, ensuring they don't bypass deep structural learning.

Optimize Enterprise Spending: Since adoption is cementing at nearly 70%, shift focus from "trial periods" to long-term bulk enterprise licensing to maximize ROI.

Implement AI-Specific Code-Review Audits: Lean into the developer consensus of "Pragmatic Skepticism" by formalizing security and quality gates specifically for AI-generated code snippets.