def team_win_rate(matches):
    total_matches = matches["team1"].value_counts() + matches["team2"].value_counts()
    wins = matches["winner"].value_counts()
    win_rate = (wins / total_matches) * 100
    return win_rate.sort_values(ascending=False)
