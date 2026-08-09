import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc

# Read the data
df = pd.read_csv("output/formatted_sales_data.csv")


#convert the data to datetime and sort according to the date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


# create the line chart
fig = px.line(
    df, 
    x = "date",
    y = "sales",
    title = "Pink Morsel Sales Overtime"
) 


# add axis label
fig.update_layout(
    xaxis_title = "Date",
    yaxis_title = "Sales"
)

#create dash create and layout
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Pink Morsel Sales"),

    dcc.Graph(
        id="sales_line_chart",
        figure = fig
    )
])

# run the application
if __name__ == "__main__":
    app.run(debug=True)