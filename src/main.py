import os
import logging

from data_loader import load_data
from player_analysis import top_scorers
from team_analysis import team_win_rate
from visualizations import plot_top_scorers, plot_team_win_rate



# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- MAIN FUNCTION ----------------
def main():
    logging.info("IPL Sports Analytics Pipeline Started")

    # 1️⃣ Ensure output directories exist
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)
    logging.info("Output folders verified/created")

    # 2️⃣ Load data
    try:
        matches, deliveries = load_data()
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return

    # 3️⃣ Player analysis
    top_players = top_scorers(deliveries)
    top_players.to_csv("outputs/player_summary.csv")
    logging.info("player_summary.csv saved")

    # 4️⃣ Team analysis
    win_rate = team_win_rate(matches)
    win_rate.to_csv("outputs/team_win_rate.csv")
    logging.info("team_win_rate.csv saved")

    # 5️⃣ Visualizations
    plot_top_scorers(top_players)
    logging.info("top_scorers.png saved")

    plot_team_win_rate(win_rate)
    logging.info("team_win_rate.png saved")

    # 6️⃣ Summary report
    with open("outputs/summary_report.txt", "w") as f:
        f.write("IPL Sports Analytics Summary\n\n")
        f.write("Top Players:\n")
        f.write(top_players.to_string())
        f.write("\n\nTeam Win Rates:\n")
        f.write(win_rate.to_string())

    logging.info("summary_report.txt saved")

    logging.info("🎉 PIPELINE COMPLETED SUCCESSFULLY 🎉")

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()

