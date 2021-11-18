import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("HDI/human-development-index-escosura.csv")

filtered = df[(df["Entity"].isin(["India", "China", "Ethiopia", "United States"])) & (df["Year"]>1899) & (df["Year"]<2001)]
hdi_wide_form = filtered.pivot(index="Entity", columns="Year", values="Historical Index of Human Development (Prados de la Escosura)")

graph = sns.relplot(data=hdi_wide_form.transpose(), kind="line")
graph.set_ylabels("HDI")
plt.show()