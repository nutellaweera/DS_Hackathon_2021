import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Emissions/CO2.csv")
filtered = df[(df["country"].isin(["India", "China", "Ethiopia", "United States"])) & (df["year"]<2000) & (df["year"]>1899)].filter(items=["year", "country", "share_global_co2", "population"])
world = df[(df["country"].isin(["World"])) & (df["year"]<2000) & (df["year"]>1899)].filter(items=["year", "population"])

share_of_pop = []
for index, row in filtered.iterrows():
    world_pop = world.loc[world["year"] == row["year"]]["population"].iloc[0]
    share_of_pop.append(row["population"]/world_pop * 100)

filtered["share_of_population"] = share_of_pop
filtered["share_global_co2"] = filtered["share_global_co2"].fillna(0)

graph = sns.FacetGrid(filtered, col="country", hue="year")
graph.map(sns.scatterplot, "share_of_population", "share_global_co2")
graph.set_axis_labels("Share of world population (%)", "Share of global CO2 (%)")
graph.set(xticks=[5,10,15,20,25,30], yticks=[25,50,75])
graph.tight_layout()
graph.savefig("Emissions/share_of_population_vs_emissions.png")
plt.show()
