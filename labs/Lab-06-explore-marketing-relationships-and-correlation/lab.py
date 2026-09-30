from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "campaign_performance.csv"); df["channel"] = df["channel"].astype("category")
sns.set_theme(style="whitegrid")
fig,ax=plt.subplots(figsize=(8.5,5.2)); sns.scatterplot(data=df,x="spend",y="conversions",hue="channel",ax=ax); sns.regplot(data=df,x="spend",y="conversions",scatter=False,ci=None,color="#111827",ax=ax); ax.set_title("Campaign spend and conversions"); ax.set_xlabel("Spend (SGD)"); plt.tight_layout(); plt.savefig(OUT / "spend_conversions.png", dpi=160); plt.close()
num=["spend","impressions","clicks","conversions","revenue"]
g=sns.pairplot(df[num],corner=True,plot_kws={"s":18,"alpha":.55}); g.fig.suptitle("Campaign metric relationships",y=1.02); g.savefig(OUT / "pairplot.png",dpi=130); plt.close("all")
corr=df[num].corr(); plt.figure(figsize=(7,5.5)); sns.heatmap(corr,annot=True,cmap="vlag",center=0,vmin=-1,vmax=1); plt.title("Pearson correlation matrix"); plt.tight_layout(); plt.savefig(OUT / "correlation_heatmap.png",dpi=160); plt.close()
corr.to_csv(OUT / "correlation_matrix.csv")
(OUT / "interpretation.md").write_text("The strongest correlations identify linear co-movement in this synthetic sample. They do not establish that increasing one metric causes another because channel mix, audience quality and campaign design may confound the relationship.\n",encoding="utf-8")
print(f"PASS: relationship pack saved to {OUT}")
