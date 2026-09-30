# Lab 01: Profile and Clean Retail Transactions

Alignment: LO1

## Scenario

Audit a synthetic omnichannel retail extract, repair missing and invalid values, remove duplicate records and preserve an exception log.

## Deliverable

A clean retail DataFrame, data-quality summary and before/after revenue comparison chart.

## Files

- `lab.py` — complete runnable Python analysis.
- `retail_transactions.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Open the lab folder and inspect the CSV and data dictionary before running code.
   - `Review README.md and retail_transactions.csv`
2. Create a virtual environment or use Google Colab, then install the required libraries.
   - `python3 -m pip install pandas matplotlib seaborn scikit-learn`
3. Load the CSV, parse order_date and inspect shape, dtypes, head and missing-value counts.
   - `pd.read_csv('retail_transactions.csv', parse_dates=['order_date'])`
4. Flag missing keys, duplicate order_id values, non-positive units and implausible unit prices.
   - `Build Boolean masks and an exceptions DataFrame`
5. Apply the documented cleaning rules without altering the source CSV.
   - `drop_duplicates, fillna, clip and astype`
6. Create revenue and compare revenue by channel before and after cleaning.
   - `assign(revenue=lambda d: d.units*d.unit_price)`
7. Save clean_data.csv, quality_report.csv and the comparison chart.
   - `python3 lab.py`
8. Write a two-sentence interpretation that distinguishes corrected records from business findings.
   - `Complete the Evidence section in README.md`

## Acceptance criteria

The script runs without error, clean_data.csv has unique order IDs, critical fields are complete and the quality report reconciles every change.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
