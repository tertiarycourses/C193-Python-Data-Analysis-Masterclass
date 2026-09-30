from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE=Path(__file__).resolve().parent; OUT=BASE/"outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(BASE/"energy_demand_hourly.csv",parse_dates=["timestamp"]).set_index("timestamp").sort_index()
duplicate_count=df.index.duplicated().sum(); expected=pd.date_range(df.index.min(),df.index.max(),freq="h"); missing=expected.difference(df.index)
df=df[~df.index.duplicated(keep="first")].reindex(expected); df.index.name="timestamp"; df["demand_kw"]=df["demand_kw"].interpolate(limit=3)
daily=df["demand_kw"].resample("D").agg(mean_kw="mean",max_kw="max",energy_kwh="sum"); weekly=df["demand_kw"].resample("W").agg(energy_kwh="sum",peak_kw="max")
daily["rolling_7d_mean"]=daily["mean_kw"].rolling(7,min_periods=3).mean(); threshold=daily["max_kw"].quantile(.95); peaks=daily[daily["max_kw"]>threshold]
ax=daily[["max_kw","rolling_7d_mean"]].plot(figsize=(10,5),color=["#4F46E5","#0F766E"]); ax.scatter(peaks.index,peaks["max_kw"],color="#DC2626",label="Peak day",zorder=5); ax.set_title("Daily peak energy demand and trailing baseline"); ax.set_ylabel("Demand (kW)"); ax.legend(); plt.tight_layout(); plt.savefig(OUT/"energy_demand_monitor.png",dpi=160); plt.close()
daily.to_csv(OUT/"daily_summary.csv"); weekly.to_csv(OUT/"weekly_summary.csv"); peaks.to_csv(OUT/"peak_days.csv"); pd.DataFrame({"duplicate_timestamps":[duplicate_count],"missing_intervals":[len(missing)]}).to_csv(OUT/"time_index_audit.csv",index=False)
assert df.index.is_monotonic_increasing and df.index.is_unique
print(f"PASS: {len(missing)} missing intervals repaired; outputs saved to {OUT}")
