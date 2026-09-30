# Lab 10: Capstone: Public Health Insight and Regression Review

Alignment: LO1–LO5

## Scenario

Prepare, visualise and model synthetic student-health indicators, then review the credibility of the evidence for a programme decision.

## Deliverable

A complete capstone pack with clean data, summaries, visual dashboard, linear model, residual review and stakeholder brief.

## Files

- `lab.py` — complete runnable Python analysis.
- `student_health.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Frame the decision: which modifiable indicators are associated with wellbeing score?
   - `Write the analytical question before opening results`
2. Load and profile the synthetic student-health data; document missingness and ranges.
   - `read_csv, info, describe and isna`
3. Clean data using explicit rules and retain excluded records in an audit file.
   - `Boolean validity mask`
4. Create group summaries and truthful charts for activity, nutrition and wellbeing.
   - `groupby, bar, scatter and heatmap`
5. Split data into train/test sets and fit a linear regression model.
   - `train_test_split and LinearRegression`
6. Evaluate R-squared, MSE and residual patterns on held-out data.
   - `r2_score, mean_squared_error and residual plot`
7. Interpret coefficients as model associations, not causal effects.
   - `Create model_summary.csv and stakeholder_brief.md`
8. Run the credibility checklist for sampling, confounding, measurement and reproducibility.
   - `Complete credibility_review.csv`
9. Package all outputs and confirm another learner can reproduce them with one command.
   - `python3 lab.py`

## Acceptance criteria

The script reproduces every output, test-set metrics and residuals are reported, causal claims are avoided and limitations are explicit in the stakeholder brief.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
