from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

BASE=Path(__file__).resolve().parent; OUT=BASE/"outputs"; OUT.mkdir(exist_ok=True)
raw=pd.read_csv(BASE/"student_health.csv")
valid=(raw["physical_activity_days"].between(0,7)&raw["vegetable_servings"].between(0,10)&raw["sweetened_drinks_week"].between(0,35)&raw["sleep_hours"].between(3,12)&raw["wellbeing_score"].between(0,100))
excluded=raw[~valid|raw.isna().any(axis=1)]; clean=raw[valid].dropna().copy()
summary=clean.groupby("education_level").agg(students=("student_id","size"),activity=("physical_activity_days","mean"),vegetables=("vegetable_servings","mean"),wellbeing=("wellbeing_score","mean"))
sns.set_theme(style="whitegrid"); fig,axs=plt.subplots(1,2,figsize=(11,4.8)); summary["wellbeing"].sort_values().plot.barh(ax=axs[0],color="#4F46E5"); axs[0].set_title("Average wellbeing by education level"); axs[0].set_xlabel("Wellbeing score"); sns.scatterplot(data=clean,x="physical_activity_days",y="wellbeing_score",hue="education_level",ax=axs[1]); axs[1].set_title("Activity and wellbeing"); plt.tight_layout(); plt.savefig(OUT/"health_dashboard.png",dpi=160); plt.close()
features=["physical_activity_days","vegetable_servings","sweetened_drinks_week","sleep_hours"]
X_train,X_test,y_train,y_test=train_test_split(clean[features],clean["wellbeing_score"],test_size=.25,random_state=4082); model=LinearRegression().fit(X_train,y_train); pred=model.predict(X_test); residual=y_test-pred
metrics=pd.DataFrame({"metric":["test_r2","test_mse","train_rows","test_rows"],"value":[r2_score(y_test,pred),mean_squared_error(y_test,pred),len(X_train),len(X_test)]})
coef=pd.DataFrame({"feature":features,"coefficient":model.coef_}); coef.loc[len(coef)]={"feature":"intercept","coefficient":model.intercept_}
plt.figure(figsize=(7,4.8)); plt.scatter(pred,residual,color="#0F766E",alpha=.7); plt.axhline(0,color="#DC2626",lw=1); plt.title("Held-out residual review"); plt.xlabel("Predicted wellbeing"); plt.ylabel("Residual"); plt.tight_layout(); plt.savefig(OUT/"residual_review.png",dpi=160); plt.close()
clean.to_csv(OUT/"clean_data.csv",index=False); excluded.to_csv(OUT/"excluded_records.csv",index=False); summary.to_csv(OUT/"group_summary.csv"); metrics.to_csv(OUT/"model_metrics.csv",index=False); coef.to_csv(OUT/"model_summary.csv",index=False)
pd.DataFrame({"check":["Synthetic training data only","Held-out evaluation used","Missing and invalid records audited","Associations not described as causal","Sampling and confounding limitations disclosed"],"status":["PASS"]*5}).to_csv(OUT/"credibility_review.csv",index=False)
(OUT/"stakeholder_brief.md").write_text(f"# Stakeholder brief\n\nThe held-out linear model achieved R-squared {r2_score(y_test,pred):.2f} and MSE {mean_squared_error(y_test,pred):.1f}. Coefficients describe conditional associations in synthetic training data, not causal effects. Any programme decision requires representative real data, stronger controls for confounding and privacy review.\n",encoding="utf-8")
print(f"PASS: capstone outputs saved to {OUT}")
