from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
raw = pd.read_csv(BASE / "retail_transactions.csv", parse_dates=["order_date"])
exceptions = pd.DataFrame({
    "missing_order_id": [raw["order_id"].isna().sum()],
    "duplicate_order_id": [raw["order_id"].duplicated(keep=False).sum()],
    "missing_channel": [raw["channel"].isna().sum()],
    "non_positive_units": [(raw["units"] <= 0).sum()],
    "implausible_price": [((raw["unit_price"] < 1) | (raw["unit_price"] > 1000)).sum()],
})
clean = (raw.dropna(subset=["order_id", "order_date"])
           .drop_duplicates("order_id", keep="first")
           .assign(channel=lambda d: d["channel"].fillna("Unknown"),
                   units=lambda d: d["units"].clip(lower=1),
                   unit_price=lambda d: d["unit_price"].clip(lower=1, upper=1000)))
clean["units"] = clean["units"].astype(int)
clean["revenue"] = clean["units"] * clean["unit_price"]
before = raw.assign(revenue=raw["units"].clip(lower=0) * raw["unit_price"].clip(lower=0)).groupby("channel", dropna=False)["revenue"].sum()
after = clean.groupby("channel")["revenue"].sum()
pd.concat({"Before cleaning": before, "After cleaning": after}, axis=1).fillna(0).plot.bar(figsize=(9,5), color=["#94A3B8", "#0F766E"])
plt.title("Revenue by channel: data-quality impact"); plt.ylabel("Revenue (SGD)"); plt.xticks(rotation=0); plt.tight_layout(); plt.savefig(OUT / "revenue_quality_comparison.png", dpi=160); plt.close()
clean.to_csv(OUT / "clean_data.csv", index=False); exceptions.to_csv(OUT / "quality_report.csv", index=False)
assert clean["order_id"].is_unique and clean[["order_id", "order_date"]].notna().all().all()
print(f"PASS: {len(raw)} raw rows -> {len(clean)} clean rows; outputs saved to {OUT}")
