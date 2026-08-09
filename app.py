import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc, Input, Output

# Read the data
df = pd.read_csv("output/formatted_sales_data.csv")


#convert the data to datetime and sort according to the date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")







#create dash create and layout
app = Dash(__name__)
app.title = "Pink Morsel Sales"
app.layout = html.Div(
    className="app-container",
    children=[

        # Header
        html.Header(
            className="header",
            children=[
                html.Div(
                    className="header-content",
                    children=[

                        html.Div(
                            "QUANTIUM DATA VISUALISATION",
                            className="brand"
                        ),

                        html.H1(
                            "Pink Morsel Analytics",
                            className="title"
                        ),

                        html.P(
                            "Explore sales performance across regions "
                            "before and after the price increase.",
                            className="subtitle"
                        ),
                    ]
                )
            ]
        ),

        # Main content
        html.Main(
            className="main-content",
            children=[

                # Region filter
                html.Div(
                    className="filter-card",
                    children=[

                        html.Div(
                            "SELECT REGION",
                            className="section-label"
                        ),

                        dcc.RadioItems(
                            id="region-selector",

                            options=[
                                {
                                    "label": "North",
                                    "value": "north"
                                },
                                {
                                    "label": "East",
                                    "value": "east"
                                },
                                {
                                    "label": "South",
                                    "value": "south"
                                },
                                {
                                    "label": "West",
                                    "value": "west"
                                },
                                {
                                    "label": "All",
                                    "value": "all"
                                },
                            ],

                            value="all",

                            inline=True,

                            className="radio-container",

                            labelClassName="radio-item"
                        ),
                    ]
                ),

                # Chart
                html.Div(
                    className="chart-card",
                    children=[

                        html.H2(
                            "Sales Performance",
                            className="chart-title"
                        ),

                        html.P(
                            "Pink Morsel sales over time",
                            className="chart-description"
                        ),

                        dcc.Graph(
                            id="sales-chart"
                        ),
                    ]
                ),

                # Information section
                html.Div(
                    className="info-card",
                    children=[

                        html.H3(
                            "Price Increase",
                            className="info-title"
                        ),

                        html.P(
                            "The Pink Morsel price increased on "
                            "15 January 2021. Use the chart above "
                            "to compare sales before and after "
                            "the price change.",
                            className="info-text"
                        ),
                    ]
                ),
            ]
        )
    ]
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)

def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[
            df['region'] == selected_region
        ]

    # create the line chart
    fig = px.line(
        df, 
        x = "date",
        y = "sales",
        title = "Pink Morsel Sales Overtime"
    ) 

    #create chart
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=""
    )

    #add price increase marker
    fig.add_vline(
        x=pd.Timestamp("2021-01-15"),
        line_dash="dash",
        line_width=2
    )

    #add annotaion
    fig.add_annotation(
        x=pd.Timestamp("2021-01-15"),
        y=1,
        yref="paper",
        text="Price increase * 15 Jan 2021",
        showarrow=False,
        yanchor="bottom"
    )

    # add axis label
    fig.update_layout(
        xaxis_title = "Date",
        yaxis_title = "Sales",
        template="plotly_white",
        hovermode="x unified",
        margin=dict(
            l=60,
            r=30,
            t=20,
            b=60
        )
    )

    return fig

    

# run the application
if __name__ == "__main__":
    app.run(debug=True)