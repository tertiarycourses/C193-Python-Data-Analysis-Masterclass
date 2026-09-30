# Lab 09: Build a Reusable pandas Analytics Pipeline

Alignment: LO5

## Scenario

Refactor a fulfilment analysis into small testable functions connected with pipe, assign and vectorised transformations.

## Deliverable

A reproducible analytics pipeline, validation log and late-delivery risk chart.

## Files

- `lab.py` — complete runnable Python analysis.
- `fulfilment_orders.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load fulfilment data and define the expected schema and allowed categories.
   - `EXPECTED_COLUMNS and validation function`
2. Write a validate_input function that raises clear errors before analysis.
   - `def validate_input(df): ...`
3. Write pure functions for cleaning, feature engineering and summarisation.
   - `def clean(df), add_features(df), summarise(df)`
4. Chain the functions with pipe and assign.
   - `df.pipe(validate_input).pipe(clean).pipe(add_features)`
5. Use vectorised np.select for risk bands; reserve apply for a justified custom label.
   - `np.select and DataFrame.apply`
6. Add assertions for row count, non-negative duration and valid risk categories.
   - `assert ...`
7. Save outputs and a late-rate chart by warehouse.
   - `python3 lab.py`

## Acceptance criteria

The pipeline can be re-run from raw input, validation fails loudly on broken schema, assertions pass and every output is derived without manual edits.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
