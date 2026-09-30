from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "monthly_retail.csv", parse_dates=["month"])
assert not df.duplicated(["month","region"]).any()
pivot = df.pivot(index="month", columns="region", values="revenue")
ax=pivot.plot.line(marker="o", figsize=(9,5), color=["#0F766E","#4F46E5","#F59E0B"]); ax.set_title("Monthly revenue by region"); ax.set_ylabel("Revenue (SGD)"); ax.set_xlabel(""); plt.tight_layout(); plt.savefig(OUT / "monthly_trend.png", dpi=160); plt.close()
annual=df.groupby("region")["revenue"].sum().sort_values(); annual.plot.barh(figsize=(8,4.5), color="#4F46E5"); plt.title("Annual revenue comparison"); plt.xlabel("Revenue (SGD)"); plt.xlim(left=0); plt.tight_layout(); plt.savefig(OUT / "regional_comparison.png", dpi=160); plt.close()
variance=df.groupby("region").agg(revenue=("revenue","sum"),target=("target","sum")); variance["variance"]=variance["revenue"]-variance["target"]
colors=["#0F766E" if v>=0 else "#DC2626" for v in variance["variance"]]; variance["variance"].plot.bar(figsize=(8,4.5), color=colors); plt.axhline(0,color="#334155",lw=1); plt.title("Revenue variance to target"); plt.ylabel("Variance (SGD)"); plt.xticks(rotation=0); plt.tight_layout(); plt.savefig(OUT / "target_variance.png", dpi=160); plt.close()
variance.to_csv(OUT / "variance_summary.csv")
(OUT / "chart_rationale.md").write_text("# Chart rationale\n\n- Line: ordered monthly trend.\n- Horizontal bar: category magnitude comparison with zero baseline.\n- Diverging bar: direction and size of target variance.\n", encoding="utf-8")
print(f"PASS: three management charts and rationale saved to {OUT}")
