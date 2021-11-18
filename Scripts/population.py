import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def convert_to_float(val):
    if val.endswith("M"):
        return float(val[:-1])
    if val.endswith("B"):
        return float(val[:-1]) * 1000
    return float(val)

def gen_population_over_time():
    df = pd.read_csv("Datasets/population_total.csv")
    filtered = df[df["country"].isin(["India", "China", "Ethiopia", "United States"])].filter(items=(["country"]+[str(n) for n in range(1900, 2001)]))
    #print("Num null values: ", filtered.isnull().values.ravel().sum())

    filtered.set_index('country', inplace=True)

    for col in filtered.columns:
        filtered[col] = filtered[col].apply(convert_to_float)

    graph = sns.relplot(data=filtered.transpose(), kind="line")
    graph.set_xlabels("Year")
    graph.set_ylabels("Population (M)")
    graph.set_xticklabels(step=10)
    plt.savefig('Graphs/population_over_time.png')
    #plt.show() 