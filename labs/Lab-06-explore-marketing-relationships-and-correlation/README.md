# Lab 06: Explore Marketing Relationships and Correlation

Alignment: LO3

## Scenario

Use scatter, regression, pair plots and a correlation heatmap to explore marketing performance without causal overclaim.

## Deliverable

A relationship-analysis pack with scatter/regression plot, pair plot, heatmap and evidence statement.

## Files

- `lab.py` — complete runnable Python analysis.
- `campaign_performance.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load campaign data and classify channel as categorical.
   - `read_csv and astype('category')`
2. Inspect distributions and extreme values before plotting relationships.
   - `describe and quantile`
3. Create a scatter plot of spend versus conversions coloured by channel.
   - `sns.scatterplot`
4. Overlay a regression line for descriptive guidance only.
   - `sns.regplot(scatter=False)`
5. Create a pair plot for numerical fields and a correlation heatmap with annotations.
   - `sns.pairplot and sns.heatmap`
6. Identify the strongest linear association and state why it does not prove causation.
   - `corr().abs() and an interpretation note`
7. Save the correlation table and all graphics.
   - `python3 lab.py`

## Acceptance criteria

The graphics render, correlation values are reproducible and the interpretation explicitly separates association from causation.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
