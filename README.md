# Python Data Analysis Masterclass

Prepare, transform, visualise and analyse real-world business data with Python, pandas, Matplotlib, Seaborn and scikit-learn.

| Course detail | Information |
|---|---|
| Course code | `C193` |
| Programme | Non-WSQ |
| Duration | 2 days · 15 hours (9:30am – 5:30pm) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/python-data-analysis-masterclass.html) |

## About the course

This hands-on masterclass takes you through the full Python data analysis workflow: framing the
decision, preparing and cleaning data, integrating and summarising it, choosing truthful charts,
running statistical and time-series analysis, and building a reusable analysis pipeline with a
linear regression model. Every concept is practised in a runnable lab built on realistic
synthetic data, and the course closes with a capstone that ties the whole workflow together.

## Learning outcomes

By the end of the course you will be able to:

- **LO1** — Prepare data for analysis with pandas.
- **LO2** — Transform and integrate data for analysis.
- **LO3** — Gain insights from clear, truthful data visualizations.
- **LO4** — Perform statistical and time-series analysis.
- **LO5** — Perform advanced analysis and interpret results credibly.

## Topics covered

| Topic | Focus |
|---|---|
| 1. Data Preparation | pandas foundations, import/export, selection, filtering and cleaning |
| 2. Data Transformation | concat, merge, sort, groupby, aggregation and pivot tables |
| 3. Data Visualization | pandas plots, Matplotlib, Seaborn, chart choice and visual integrity |
| 4. Data Analysis | data types, descriptive statistics, covariance, correlation and time series |
| 5. Advanced Data Analytics | pipe, apply, custom functions, linear regression and credibility review |

## Labs

Each lab folder holds a `README.md`, a self-contained `lab.py` and its synthetic CSV data. See the
[labs index](labs/README.md).

| Lab | Topic |
|---|---|
| [Lab 01 — Profile and Clean Retail Transactions](labs/Lab-01-profile-and-clean-retail-transactions/README.md) | 1 |
| [Lab 02 — Select, Filter and Segment Customer Orders](labs/Lab-02-select-filter-and-segment-customer-orders/README.md) | 1 |
| [Lab 03 — Integrate Orders, Products and Targets](labs/Lab-03-integrate-orders-products-and-targets/README.md) | 2 |
| [Lab 04 — Summarise Service Operations with GroupBy and Pivot](labs/Lab-04-summarise-service-operations-with-groupby-and-pivot/README.md) | 2 |
| [Lab 05 — Visualise Monthly Retail Performance](labs/Lab-05-visualise-monthly-retail-performance/README.md) | 3 |
| [Lab 06 — Explore Marketing Relationships and Correlation](labs/Lab-06-explore-marketing-relationships-and-correlation/README.md) | 3 |
| [Lab 07 — Analyse Service Quality Distributions](labs/Lab-07-analyse-service-quality-distributions/README.md) | 4 |
| [Lab 08 — Resample and Monitor Energy Demand](labs/Lab-08-resample-and-monitor-energy-demand/README.md) | 4 |
| [Lab 09 — Build a Reusable pandas Analytics Pipeline](labs/Lab-09-build-a-reusable-pandas-analytics-pipeline/README.md) | 5 |
| [Lab 10 — Capstone: Public Health Insight and Regression Review](labs/Lab-10-capstone-public-health-insight-and-regression-review/README.md) | 1–5 |

### Running a lab

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd labs/Lab-01-profile-and-clean-retail-transactions
python3 lab.py
```

Google Colab works too — upload the lab folder and run `lab.py`.

## Courseware (v1.0)

| Artifact | Editable | PDF |
|---|---|---|
| Slide deck | [PPTX](courseware/Python%20Data%20Analysis%20Masterclass-v1.0.pptx) | [PDF](courseware/Python%20Data%20Analysis%20Masterclass-v1.0.pdf) |
| Lesson Plan | [DOCX](courseware/LP-Python%20Data%20Analysis%20Masterclass.docx) | [PDF](courseware/LP-Python%20Data%20Analysis%20Masterclass.pdf) |
| Learner Guide | [DOCX](courseware/LG-Python%20Data%20Analysis%20Masterclass.docx) | [PDF](courseware/LG-Python%20Data%20Analysis%20Masterclass.pdf) |
| Learner Guide (Markdown) | [LG-Python Data Analysis Masterclass (C193).md](LG-Python%20Data%20Analysis%20Masterclass%20(C193).md) | — |

## Distribution

This repository publishes the learner-facing courseware and labs. All datasets are synthetic.
Build scripts and trainer-only reference material are kept out of the public repository.

---

Provided by [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg) · UEN 201200696W
