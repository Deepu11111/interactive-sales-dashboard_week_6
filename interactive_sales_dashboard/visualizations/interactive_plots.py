import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("../data/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Monthly Sales Trend
monthly_sales = df.resample("ME",on="Date")["Total_Sales"].sum().reset_index()
fig_line = px.line(monthly_sales,x="Date",y="Total_Sales",title="Monthly Sales Trend",markers=True,template="plotly_white")

# Sales By Region 
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()
fig_bar = px.bar(region_sales,x="Region",y="Total_Sales",color="Region",title="Sales by Region",template="plotly_white")

# Product Share (pie chart)
product_sales  = df.groupby("Product")["Total_Sales"].sum().reset_index()
fig_pie = px.pie(product_sales,names="Product",values="Total_Sales",title="Product Sales Distribution")

# Quantity vs Total Sales
fig_scatter = px.scatter(df,x="Quantity",y="Total_Sales",color="Region",hover_data=["Product","Customer_ID"],title="Quantity vs Total Sales",template="plotly_white")

# Region Filter Dropdown 
fig_dropdown = go.Figure()

for region in df["Region"].unique():
    filtered = df[df["Region"]==region]
    fig_dropdown.add_trace(
        go.Scatter(
            x=filtered["Date"],
            y=filtered["Total_Sales"],
            mode = "lines",
            name = region,
            visible = True
        )
    )

fig_dropdown.update_layout(
    title="Region-wise Sales Trend",
    xaxis_title="Date",
    yaxis_title="Total Sales",
    template = "plotly_white"
)

# Save All as Html
with open("interactive_dashboard.html", "w") as f:
    f.write(fig_line.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig_bar.to_html(full_html=False, include_plotlyjs=False))
    f.write(fig_pie.to_html(full_html=False, include_plotlyjs=False))
    f.write(fig_scatter.to_html(full_html=False, include_plotlyjs=False))
    f.write(fig_dropdown.to_html(full_html=False, include_plotlyjs=False))

print("Interactive Dashboard Created Successfully!")