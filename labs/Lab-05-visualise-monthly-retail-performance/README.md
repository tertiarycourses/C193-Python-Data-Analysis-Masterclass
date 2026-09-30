# Lab 05: Visualise Monthly Retail Performance

Alignment: LO3

## Scenario

Select chart types for time trend, category comparison and target variance, then annotate the decision signal.

## Deliverable

A three-chart management pack: monthly trend, regional comparison and variance waterfall-style bar chart.

## Files

- `lab.py` — complete runnable Python analysis.
- `monthly_retail.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load monthly_retail.csv, parse month and validate one row per month-region.
   - `read_csv, to_datetime, duplicated`
2. Pivot revenue by region and create a line chart with shared units and restrained colours.
   - `pivot(...).plot.line`
3. Aggregate annual revenue and create a sorted horizontal bar chart.
   - `groupby and barh`
4. Calculate revenue minus target and colour positive/negative variances consistently.
   - `np.where(variance >= 0, ...)`
5. Add titles, units, source period and a concise annotation for the strongest signal.
   - `Axes.set_title, set_ylabel and annotate`
6. Remove non-data ink, use honest axes and export at 160 dpi.
   - `plt.savefig(..., dpi=160, bbox_inches='tight')`
7. Record why each chart matches its analytical question.
   - `Complete chart_rationale.md`

## Acceptance criteria

All three charts render, labels and units are complete, bars use a zero baseline and the rationale connects chart choice to the question.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
