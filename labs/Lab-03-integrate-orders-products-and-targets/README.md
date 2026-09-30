# Lab 03: Integrate Orders, Products and Targets

Alignment: LO2

## Scenario

Join transaction, product and monthly-target tables with validated keys, cardinality checks and unmatched-record evidence.

## Deliverable

An enriched order table, join audit and product-category performance chart.

## Files

- `lab.py` — complete runnable Python analysis.
- `orders.csv + products.csv + targets.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Inspect the grain and key uniqueness of each source file.
   - `nunique, duplicated and value_counts`
2. Validate the products key as many-to-one before merging.
   - `merge(..., validate='many_to_one', indicator=True)`
3. Create a month key and merge monthly regional targets.
   - `df['month'] = df.order_date.dt.to_period('M').astype(str)`
4. Review unmatched and duplicated records instead of silently dropping them.
   - `Filter _merge != 'both'`
5. Concatenate an approved late-arriving order batch.
   - `pd.concat([...], ignore_index=True)`
6. Calculate revenue, attainment and category contribution.
   - `assign and groupby`
7. Save the enriched data, join audit and chart.
   - `python3 lab.py`

## Acceptance criteria

Row counts reconcile, the many-to-one validations pass, unmatched keys are reported and totals before/after integration are explained.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
