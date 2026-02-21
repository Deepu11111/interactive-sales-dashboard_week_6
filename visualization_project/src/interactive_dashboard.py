import pandas as pd
import plotly.express as px


df = pd.read_csv("../data/sales_data.csv")

# Interactive Box Plot
fig1 = px.box(df,x="Region",y="Total_Sales",
              color="Region",
              title="Interactive Sales Distribution by Region",
              hover_data=df.columns
              )

fig1.show()

import plotly.graph_objects as go

correlation = df.corr(numeric_only=True)

fig2 = go.Figure(
    data = go.Heatmap(
        z=correlation.values,
        x=correlation.columns,
        y=correlation.columns,
        colorscale="RdBu"
    )
)

fig2.update_layout(title="Interactive Correlation Heatmap")
fig2.show()

# Combine Multiple charts into Dashboard Layout

from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2 ,cols=2,
    subplot_titles=("Sales by Region","Sales Trend","Quantity Distribution","Sales vs Profit")
)

# Bar 
fig.add_trace(
    px.bar(df ,x="Region",y="Total_Sales".data[0],row=1 ,col=1)
)

# Line
fig.add_trace(
    px.line(df,x="Date",y="Total_Sales".data[0],row=1,col=2)
)

# Histogram
fig.add_trace(
    px.histogram(df,x="Quantity").data[0],row=2,col=2
)

fig.update_layout(
    height = 800,
    width = 1000,
    title_text = "Sales Dashboard"
)

fig.write_html("../outputs/dashboard.html")
fig.show()