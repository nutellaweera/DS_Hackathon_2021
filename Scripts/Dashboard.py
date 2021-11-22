import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("Datasets/all-in-one.csv")

#colors = {"background": "#4E8B9D", "text": "#2C2C22"}

app.layout = html.Div(
    [
        html.H1(
            "Share of global co2 vs social growth",
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="factor-dropdown",
                            options=[
                                {"label": factor, "value": factor} for factor in ["hdi", "population","life_expectancy"]
                            ],
                            className="dropdown",
                            value="population",
                        ),
                    ]
                ),
            ],
            className="row",
        ),
        html.Div(dcc.Graph(id="factors-over-time"), className="chart"),
        dcc.RangeSlider(
            "year-slider",
            min=df.year.min(), # dynamically select minimum and maximum years from the dataset.
            max=df.year.max(),
            marks={year: str(year) for year in range(1900, 2000, 10)},
            value=[1901, 1999],
        ),
    ],
    className="container",
)


@app.callback(
    Output("factors-over-time", "figure"),
    Input("factor-dropdown", "value"),
    Input("year-slider", "value"),
)
def update_figure(selected_factor, selected_years):
    filtered = df[(df["year"]>selected_years[0]) & (df["year"]<selected_years[1])]
    fig = px.scatter(
        filtered,
        x="share_global_co2",
        y=selected_factor,
        color="country",
    )

    return fig

app.run_server(debug=True)