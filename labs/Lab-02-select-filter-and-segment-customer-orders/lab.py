from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "customer_orders.csv").set_index("customer_id")
named = df.loc[["C0005", "C0012", "C0027"], ["region", "orders_12m", "avg_order_value"]]
positional = df.iloc[:10, :5]
high_value = df[(df["avg_order_value"] >= 180) & (df["days_since_last_order"] <= 45)]
at_risk = df[(df["days_since_last_order"] > 90) & (df["orders_12m"].between(1, 5))]
df["segment"] = "Core"
df.loc[high_value.index, "segment"] = "High value"
df.loc[at_risk.index, "segment"] = "At risk"
summary = df.groupby("segment").agg(customers=("orders_12m", "size"), avg_order_value=("avg_order_value", "mean")).sort_values("avg_order_value")
summary["avg_order_value"].plot.barh(figsize=(8,4.8), color="#4F46E5")
plt.title("Average order value by customer segment"); plt.xlabel("Average order value (SGD)"); plt.xlim(left=0); plt.tight_layout(); plt.savefig(OUT / "segment_value.png", dpi=160); plt.close()
named.to_csv(OUT / "loc_sample.csv"); positional.to_csv(OUT / "iloc_sample.csv"); high_value.to_csv(OUT / "high_value.csv"); at_risk.to_csv(OUT / "at_risk.csv"); summary.to_csv(OUT / "segment_summary.csv")
assert summary["customers"].sum() == len(df)
print(f"PASS: {len(df)} customers segmented; outputs saved to {OUT}")
