from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
orders = pd.read_csv(BASE / "orders.csv", parse_dates=["order_date"])
late = pd.read_csv(BASE / "late_orders.csv", parse_dates=["order_date"])
products = pd.read_csv(BASE / "products.csv")
targets = pd.read_csv(BASE / "targets.csv")
assert products["product_id"].is_unique
orders = pd.concat([orders, late], ignore_index=True)
orders["month"] = orders["order_date"].dt.to_period("M").astype(str)
joined = orders.merge(products, on="product_id", how="left", validate="many_to_one", indicator="product_match")
joined = joined.merge(targets, on=["region", "month"], how="left", validate="many_to_one", indicator="target_match")
joined["revenue"] = joined["units"] * joined["unit_price"]
joined["attainment"] = joined["revenue"] / joined["monthly_target"]
audit = pd.DataFrame({"check":["orders_after_concat","unmatched_products","unmatched_targets","duplicate_order_ids"], "value":[len(orders),(joined["product_match"]!="both").sum(),(joined["target_match"]!="both").sum(),joined["order_id"].duplicated().sum()]})
chart = joined.groupby("category")["revenue"].sum().sort_values()
chart.plot.barh(figsize=(8,5), color="#0F766E"); plt.title("Revenue contribution by product category"); plt.xlabel("Revenue (SGD)"); plt.xlim(left=0); plt.tight_layout(); plt.savefig(OUT / "category_revenue.png", dpi=160); plt.close()
joined.drop(columns=["product_match","target_match"]).to_csv(OUT / "enriched_orders.csv", index=False); audit.to_csv(OUT / "join_audit.csv", index=False)
assert audit.loc[audit["check"].isin(["unmatched_products","unmatched_targets","duplicate_order_ids"]), "value"].sum() == 0
print(f"PASS: {len(orders)} orders integrated; outputs saved to {OUT}")
