# Lab 08: Resample and Monitor Energy Demand

Alignment: LO4

## Scenario

Parse an hourly time series, resample it to daily and weekly frequency, calculate rolling demand and detect peaks without future leakage.

## Deliverable

Daily and weekly energy summaries, rolling-demand chart and a peak-demand exception table.

## Files

- `lab.py` — complete runnable Python analysis.
- `energy_demand_hourly.csv` — synthetic/mock pandas input data generated for this lab.
- `outputs/` — created when the script runs.

## Procedure

The full teaching procedure is in the Learner Guide. Use this lab checklist while working:

1. Load the hourly readings, parse timestamp and set a sorted DatetimeIndex.
   - `read_csv(..., parse_dates=['timestamp']).set_index('timestamp').sort_index()`
2. Check frequency, duplicates and missing hourly intervals.
   - `index.to_series().diff and asfreq('h')`
3. Resample demand to daily mean/max and weekly total.
   - `resample('D').agg(...) and resample('W').sum()`
4. Calculate a trailing seven-day rolling mean using only current and past values.
   - `rolling(7, min_periods=3).mean()`
5. Detect peak days above the 95th percentile.
   - `daily['max_kw'] > daily['max_kw'].quantile(.95)`
6. Plot daily maximum with the rolling baseline and peak markers.
   - `Matplotlib line and scatter`
7. Save summaries, exceptions and the chart.
   - `python3 lab.py`

## Acceptance criteria

The index is complete and sorted, resampled totals are explainable, rolling calculations use no future values and peak days are retained as evidence.

## Evidence

- Keep the generated CSV summaries and PNG visualization(s).
- Record one decision-ready finding and one limitation.
- Do not replace the source data; the script must reproduce the outputs from scratch.

All data in this folder is synthetic and created solely for learning.
