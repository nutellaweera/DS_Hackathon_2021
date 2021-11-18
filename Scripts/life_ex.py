import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def gen_life_ex_over_time():
    df = pd.read_csv("Datasets/life_ex.csv")

    filtered = df[(df["Entity"].isin(["India", "China", "Ethiopia", "United States"])) & (df["Year"]>1899) & (df["Year"]<2001)]
    life_wide = filtered.pivot(index="Entity", columns="Year", values="Life expectancy")

    graph = sns.relplot(data=life_wide.transpose(), kind="line")
    graph.set_ylabels("Life expectancy (years)")
    plt.savefig('Graphs/life_expectancy_over_time.png')
    #plt.show()