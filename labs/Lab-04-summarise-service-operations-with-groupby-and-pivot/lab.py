from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent; OUT = BASE / "outputs"; OUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "service_tickets.csv", parse_dates=["opened_at","resolved_at"])
df["resolution_hours"] = (df["resolved_at"] - df["opened_at"]).dt.total_seconds()/3600
df["sla_met"] = df["resolution_hours"] <= df["sla_hours"]
score = (df.groupby("support_team").agg(ticket_count=("ticket_id","size"), median_hours=("resolution_hours","median"), sla_rate=("sla_met","mean")).sort_values(["sla_rate","ticket_count"]))
by_priority = df.groupby(["support_team","priority"]).agg(tickets=("ticket_id","size"), median_hours=("resolution_hours","median"))
pivot = df.pivot_table(index="support_team", columns="priority", values="ticket_id", aggfunc="count", fill_value=0)
pivot[[c for c in ["Low","Medium","High","Critical"] if c in pivot]].plot.bar(stacked=True, figsize=(9,5), color=["#94A3B8","#38BDF8","#F59E0B","#DC2626"])
plt.title("Service-ticket workload by team and priority"); plt.ylabel("Ticket count"); plt.xticks(rotation=0); plt.tight_layout(); plt.savefig(OUT / "team_priority_workload.png", dpi=160); plt.close()
score.to_csv(OUT / "sla_scorecard.csv"); by_priority.to_csv(OUT / "team_priority_summary.csv"); pivot.to_csv(OUT / "priority_pivot.csv")
assert int(pivot.to_numpy().sum()) == len(df)
print(f"PASS: pivot reconciles to {len(df)} tickets; outputs saved to {OUT}")
