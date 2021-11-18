import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Population_historic/population_total.csv")
filtered = df[df["country"].isin(["India", "China", "Ethiopia", "United States"])].filter(items=(["country"]+[str(n) for n in range(1900, 2001)]))
print("Num null values: ", filtered.isnull().values.ravel().sum())

filtered.set_index('country', inplace=True)

def convert(val):
    if val.endswith("M"):
        return float(val[:-1])
    if val.endswith("B"):
        return float(val[:-1]) * 1000
    return float(val)

for col in filtered.columns:
    filtered[col] = filtered[col].apply(convert)

graph = sns.relplot(data=filtered.transpose(), kind="line")
graph.set_xlabels("Year")
graph.set_ylabels("Population (M)")
graph.set_xticklabels(step=10)
plt.show() 