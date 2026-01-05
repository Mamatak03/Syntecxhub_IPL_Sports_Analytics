import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_scorers(top_players):
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_players.values, y=top_players.index)
    plt.title("Top IPL Run Scorers")
    plt.xlabel("Runs")
    plt.ylabel("Player")
    plt.tight_layout()
    plt.savefig("outputs/plots/top_scorers.png")
    plt.close()

def plot_team_win_rate(win_rate):
    plt.figure(figsize=(10,6))
    win_rate.head(8).plot(kind="bar")
    plt.title("Top Team Win Rate")
    plt.ylabel("Win %")
    plt.tight_layout()
    plt.savefig("outputs/plots/team_win_rate.png")
    plt.close()
