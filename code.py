# import 
import pandas as pd
import matplotlib.pyplot as plt
# load dataset
df = pd.read_csv("club_stats.csv")
# check dataset
print(df.head())

# create new metrics
df["XG_Balance"] = (df["XG"] - df["XGA"])
df["Big_Chance_Balance"] = (df["Big_Chance_Created"] - df["Opp_Big_Chance"])
df["Shot_Dominance"] = (df["Shot_On_Target"] - df["Opp_Shots_On_Target"])

# create graph function
def make_bar_chart(column, title, ylabel):
 sorted_df = df.sort_values(column, ascending=False)
 plt.figure(figsize=(10,6))
 plt.bar(sorted_df["Team"], sorted_df[column])
 plt.xticks(rotation=45)
 plt.ylabel(ylabel)
 plt.title(title)
 plt.tight_layout()
 plt.show()

# make charts
make_bar_chart("XG_Balance", "XG_Balance_Comparison", "XG_Balance")
make_bar_chart("Big_Chance_Balance", "Big_Chance_Balance_Comparison", "Big_Chance_Balance")
make_bar_chart("Shot_Dominance", "Shot_Dominance_Comparison", "Shot_Dominance")
make_bar_chart("Possession", "Possession_Comparison", "Possession %")

# make scatter plots
plt.figure(figsize=(8,6))
plt.scatter(df["Possession"], df["XGA"])
for i in range(len(df)):
 plt.text(df["Possession"][i], df["XGA"][i], df["Team"][i])
plt.xlabel("Possession")
plt.ylabel("XGA")
plt.title("Possession vs XGA")
plt.show()

# z score analysis
metrics = ["XG_Balance", "Big_Chance_Balance", "Shot_Dominance", "Possession", "Passes"]
z_scores = df[metrics].apply(lambda x: (x-x.mean())/x.std())
z_scores["Team"] = df["Team"]
print(z_scores)

# show city only
city = z_scores[z_scores["Team"] == "Man City"]
print(city)

# save
df.to_csv("club_stats_metrics.csv", index=False)
print("project complete")