# Lab 02: Select, Filter and Segment Customer Orders

Alignment: LO1

## Scenario

Use label-based and position-based selection, Boolean filters and slicing to answer a realistic customer-retention question.

## Deliverable

Reusable customer segments and a chart comparing average order value by segment.

## Files

- `lab.py` — complete runnable Python analysis.
- `customer_orders.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load customer_orders.csv and set customer_id as the stable index.
   - `df = pd.read_csv(...).set_index('customer_id')`
2. Use loc to select named customers and columns, then use iloc for a positional audit sample.
   - `df.loc[...] and df.iloc[...]`
3. Filter recent high-value customers and at-risk customers using explicit Boolean conditions.
   - `mask = (df['days_since_last_order'] > 90) & ...`
4. Use between and isin to create transparent business segments.
   - `Series.between and Series.isin`
5. Aggregate segment size and average order value.
   - `groupby('segment').agg(...)`
6. Create a labelled bar chart and save the segment extracts.
   - `python3 lab.py`
7. Verify the segment totals do not exceed the source population.
   - `Compare unique customer counts`

## Acceptance criteria

The loc and iloc samples are saved, every segment rule is reproducible and the chart uses an honest zero baseline.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
