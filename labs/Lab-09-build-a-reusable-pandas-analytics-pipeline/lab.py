from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE=Path(__file__).resolve().parent; OUT=BASE/"outputs"; OUT.mkdir(exist_ok=True)
EXPECTED={"order_id","warehouse","promised_days","actual_days","distance_km","order_value","priority"}
def validate_input(df):
    missing=EXPECTED-set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    if not df["order_id"].is_unique: raise ValueError("order_id must be unique")
    return df.copy()
def clean(df):
    return df.dropna(subset=["warehouse","actual_days"]).assign(actual_days=lambda d:d.actual_days.clip(lower=0))
def add_features(df):
    return df.assign(delay_days=lambda d:d.actual_days-d.promised_days,
                     late=lambda d:d.actual_days>d.promised_days,
                     risk=lambda d:np.select([d.actual_days-d.promised_days>=3,d.actual_days>d.promised_days],["High","Medium"],default="Low"),
                     case_label=lambda d:d.apply(lambda r:f"{r.warehouse}-{r.priority}",axis=1))
def summarise(df):
    return df.groupby("warehouse").agg(orders=("order_id","size"),late_rate=("late","mean"),median_delay=("delay_days","median"),value=("order_value","sum")).sort_values("late_rate",ascending=False)
raw=pd.read_csv(BASE/"fulfilment_orders.csv"); enriched=raw.pipe(validate_input).pipe(clean).pipe(add_features); summary=enriched.pipe(summarise)
assert len(enriched)<=len(raw) and enriched["actual_days"].ge(0).all() and enriched["risk"].isin(["Low","Medium","High"]).all()
summary["late_rate"].sort_values().plot.barh(figsize=(8,4.8),color="#F59E0B"); plt.title("Late-delivery rate by warehouse"); plt.xlabel("Late rate"); plt.xlim(0,1); plt.tight_layout(); plt.savefig(OUT/"warehouse_late_rate.png",dpi=160); plt.close()
enriched.to_csv(OUT/"enriched_orders.csv",index=False); summary.to_csv(OUT/"warehouse_summary.csv"); pd.DataFrame({"check":["input_rows","output_rows","unique_ids","valid_risk"],"value":[len(raw),len(enriched),enriched.order_id.is_unique,enriched.risk.isin(["Low","Medium","High"]).all()]}).to_csv(OUT/"validation_log.csv",index=False)
print(f"PASS: reproducible pipeline processed {len(enriched)} rows; outputs saved to {OUT}")
