# Lab 04: Summarise Service Operations with GroupBy and Pivot

Alignment: LO2

## Scenario

Transform service-ticket data into SLA and workload summaries using named aggregations and pivot tables.

## Deliverable

A tidy SLA scorecard, priority-by-team pivot and stacked workload chart.

## Files

- `lab.py` — complete runnable Python analysis.
- `service_tickets.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load ticket data and create resolution_hours and sla_met fields.
   - `pd.to_datetime and vectorised comparison`
2. Group by support_team with named aggregations for volume, median resolution and SLA rate.
   - `groupby(...).agg(ticket_count=..., median_hours=..., sla_rate=...)`
3. Create a multi-index summary by team and priority.
   - `groupby(['support_team','priority'])`
4. Build a pivot table of ticket counts and fill only structurally missing combinations with zero.
   - `pivot_table(..., fill_value=0)`
5. Sort the scorecard by SLA rate and volume to focus management attention.
   - `sort_values`
6. Create a stacked bar chart and save all summaries.
   - `python3 lab.py`
7. Validate the pivot total equals the source ticket count.
   - `assert pivot.to_numpy().sum() == len(df)`

## Acceptance criteria

The pivot total reconciles, each metric has an explicit denominator and the SLA result is not confused with ticket volume.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
