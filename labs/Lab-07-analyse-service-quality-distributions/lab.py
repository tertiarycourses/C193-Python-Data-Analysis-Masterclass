from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(BASE / "service_quality.csv"); df["channel"]=df["channel"].astype("category")
summary=df.groupby("channel",observed=True)["resolution_minutes"].agg(count="count",mean="mean",median="median",std="std",minimum="min",q1=lambda s:s.quantile(.25),q3=lambda s:s.quantile(.75),maximum="max")
summary["range"]=summary["maximum"]-summary["minimum"]; summary["mean_median_gap"]=summary["mean"]-summary["median"]
q1,q3=df["resolution_minutes"].quantile([.25,.75]); iqr=q3-q1; low,high=q1-1.5*iqr,q3+1.5*iqr; outliers=df[(df["resolution_minutes"]<low)|(df["resolution_minutes"]>high)]
sns.set_theme(style="whitegrid"); plt.figure(figsize=(9,5)); sns.histplot(data=df,x="resolution_minutes",hue="channel",bins=24,element="step",common_bins=True); plt.title("Resolution-time distribution by channel"); plt.xlabel("Resolution time (minutes)"); plt.tight_layout(); plt.savefig(OUT/"resolution_histogram.png",dpi=160); plt.close()
plt.figure(figsize=(8,5)); sns.boxplot(data=df,x="channel",y="resolution_minutes",color="#38BDF8"); plt.title("Resolution-time spread by channel"); plt.xlabel(""); plt.ylabel("Resolution time (minutes)"); plt.tight_layout(); plt.savefig(OUT/"resolution_boxplot.png",dpi=160); plt.close()
summary.to_csv(OUT/"descriptive_statistics.csv"); outliers.to_csv(OUT/"outlier_review.csv",index=False)
print(f"PASS: {len(outliers)} candidate outliers retained for review; outputs saved to {OUT}")
