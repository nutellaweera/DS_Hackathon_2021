import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def gen_literacy_over_time():
    df = pd.read_csv("Datasets/literacy.csv")
    filtered = df[df["Country"].isin(["India", "China", "United States of America", "Ethiopia"])].filter(items=(["Country"]+['Y'+str(n) for n in range(1900, 2001)]))

    filtered.set_index('Country', inplace=True)
    graph = sns.relplot(data=filtered.transpose(), kind="line")
    graph.set_xlabels("Year")
    graph.set_ylabels("Literacy rate (%)")
    graph.set_xticklabels(step=5)
    plt.savefig('Graphs/literacy_over_time.png')
    #plt.show()