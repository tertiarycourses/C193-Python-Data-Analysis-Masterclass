# Lab 07: Analyse Service Quality Distributions

Alignment: LO4

## Scenario

Compare centre and spread across service channels and identify candidate outliers without deleting them automatically.

## Deliverable

Descriptive-statistics table, histogram, box plot and evidence-based channel comparison.

## Files

- `lab.py` — complete runnable Python analysis.
- `service_quality.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load service_quality.csv and distinguish categorical from continuous fields.
   - `select_dtypes and astype`
2. Calculate count, mean, median, standard deviation, quartiles and range by channel.
   - `groupby.describe and named agg`
3. Create histograms with common bins and scales.
   - `sns.histplot(..., hue='channel', common_bins=True)`
4. Create a box plot and calculate IQR candidate-outlier thresholds.
   - `quantile and sns.boxplot`
5. Compare the mean and median to diagnose skew.
   - `summary.assign(mean_median_gap=...)`
6. Investigate candidate outliers and retain a review file rather than dropping rows.
   - `Save outlier_review.csv`
7. Write a decision note for the operations manager.
   - `python3 lab.py`

## Acceptance criteria

Statistics reconcile to the source, candidate outliers remain traceable and the interpretation uses median when the distribution is skewed.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
