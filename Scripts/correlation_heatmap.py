import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def gen_correlation():
    df = pd.read_csv("Datasets/CO2.csv")
    filtered = df[(df["country"].isin(["India", "China", "Ethiopia", "United States"])) & (df["year"]>1950) & (df["year"]<2001)].filter(items=["year", "country", "share_global_co2", "population"])

    hdi_df = pd.read_csv("Datasets/human-development-index-escosura.csv")
    hdi_df_filtered = hdi_df[(hdi_df["Entity"].isin(["India", "China", "Ethiopia", "United States"])) & (hdi_df["Year"]>1950) & (hdi_df["Year"]<2001)]
   
    life_df = pd.read_csv("Datasets/life_ex.csv")
    life_filtered = life_df[(life_df["Entity"].isin(["India", "China", "Ethiopia", "United States"])) & (life_df["Year"]>1950) & (life_df["Year"]<2001)]
   
    hdi_col, life_col = [], []
    for index, row in filtered.iterrows():
        hdi_match = hdi_df_filtered.loc[(hdi_df_filtered["Year"] == row["year"]) & (hdi_df_filtered["Entity"] == row["country"])]["Historical Index of Human Development (Prados de la Escosura)"]
        if (len(hdi_match.values)):
            hdi_col.append(hdi_match.values[0])
        else:
            hdi_col.append(0)
        
        life_match = life_filtered.loc[(life_filtered["Year"] == row["year"]) & (life_filtered["Entity"] == row["country"])]["Life expectancy"]
        if (len(life_match.values)):
            life_col.append(life_match.values[0])
        else:
            life_col.append(0)

    filtered["hdi"] = hdi_col
    filtered["life_expectancy"] = life_col
    #print(filtered)
    # plt.matshow(filtered.corr())
    # plt.show()
    graph = sns.FacetGrid(filtered, col="year", hue="country", legend_out=True, col_wrap=8)
    graph.map(sns.scatterplot, "share_global_co2", "hdi")
    graph.set_axis_labels("Share of global CO2 (%)", "Human development idx")
    graph.tight_layout()
    graph.add_legend()
    plt.show()

gen_correlation()