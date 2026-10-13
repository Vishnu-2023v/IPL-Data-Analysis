import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load IPL match dataset
df = pd.read_csv("matches.csv")

print("IPL Dataset loaded successfully!")
print("Number of matches:", len(df))

# -------------------------------
# 1. Most Winning Teams
# -------------------------------

winning_teams = df["winner"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=winning_teams.values, y=winning_teams.index)

plt.title("Top 10 IPL Teams by Number of Wins")
plt.xlabel("Number of Wins")
plt.ylabel("Team")

plt.tight_layout()
plt.savefig("top_winning_teams.png", dpi=300)
plt.show()

# -------------------------------
# 2. Most Used Venues
# -------------------------------

venues = df["venue"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=venues.values, y=venues.index)

plt.title("Top 10 IPL Match Venues")
plt.xlabel("Number of Matches")
plt.ylabel("Venue")

plt.tight_layout()
plt.savefig("top_venues.png", dpi=300)
plt.show()

# -------------------------------
# 3. Toss Decisions
# -------------------------------

toss_decisions = df["toss_decision"].value_counts()

plt.figure(figsize=(7, 5))
toss_decisions.plot(
    kind="bar",
    title="IPL Toss Decisions"
)

plt.xlabel("Toss Decision")
plt.ylabel("Number of Matches")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("toss_decisions.png", dpi=300)
plt.show()

# -------------------------------
# Summary
# -------------------------------

print("\nIPL Analysis Summary")
print("--------------------")
print("Most successful teams:")
print(winning_teams)

print("\nMost used venues:")
print(venues)

print("\nIPL Data Analysis completed successfully!")