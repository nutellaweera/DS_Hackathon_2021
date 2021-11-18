import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Emissions/CO2.csv")
filtered = df[(df["country"].isin(["India", "China", "Ethiopia", "United States"])) & (df["year"]<2000) & (df["year"]>1899)].filter(items=["year", "country", "share_global_co2", "population"])
world = df[(df["country"].isin(["World"])) & (df["year"]<2000) & (df["year"]>1899)].filter(items=["year", "population"])
filtered.set_index('country', inplace=True)

filtered["share_global_co2"] = filtered["share_global_co2"].fillna(0)
filtered.to_csv('Emissions/CO2_countries_filtered.csv')

graph = sns.scatterplot(data=filtered, x="year", y="share_global_co2", hue="country", size="population", sizes=(20,800))
graph.set_ylabel("Share of global CO2 (%)")
plt.show()