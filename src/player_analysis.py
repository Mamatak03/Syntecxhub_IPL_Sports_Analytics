def top_scorers(deliveries, top_n=10):
    runs = deliveries.groupby("batter")["batsman_runs"].sum()
    return runs.sort_values(ascending=False).head(top_n)

