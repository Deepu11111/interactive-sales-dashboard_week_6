import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_data():
    df = pd.read_csv("data/sales_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def calculate_kpis(df):
    total_sales = df["Total_Sales"].sum()
    total_quantity = df["Quantity"].sum()
    total_customers = df["Customer_ID"].nunique()

    return total_sales,total_quantity,total_customers

def prepare_aggregations(df):
    monthly_sales=(df.resample("ME",on="Date")["Total_Sales"]
                   .sum().reset_index())

# REgion wise sales
    region_sales=( df.groupby("Region")["Total_Sales"].sum().reset_index())

# Product wise sales
    product_sales = (df.groupby("Product")["Total_Sales"].sum().reset_index())

    return monthly_sales,region_sales,product_sales

def build_dashboard(df,monthly_sales,region_sales,product_sales,
                    total_sales,total_quantity,total_customers):
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Monthly Sales Trend",
            "Sales by Region",
            "Product Distribution",
            "Quantity vs Total Sales"
        ),
        specs=[[{"type":"scatter"},{"type":"bar"}],[{"type":"pie"},{"type":"scatter"}]]
    )
    # Monthly line
    fig.add_trace(
        go.Scatter(
            x=monthly_sales["Date"],
            y=monthly_sales["Total_Sales"],
            mode="lines+markers",
            name="Monthly Sales"
        ),
        row=1, col=1
    )

    # Region Bar
    fig.add_trace(
        go.Bar(
            x=region_sales["Region"],
            y=region_sales["Total_Sales"],
            name="Region Sales"
        ),
        row=1, col=2
    )

    # Product pie
    fig.add_trace(
        go.Pie(
            labels=product_sales["Product"],
            values=product_sales["Total_Sales"],
            name="Product Share"
        ),
        row=2, col=1
    )

    # Scatter
    fig.add_trace(
        go.Scatter(
            x=df["Quantity"],
            y=df["Total_Sales"],
            mode="markers",
            name="Quantity vs Sales"
        ),
        row=2 ,col=2
    )

    # Layout Styling
    fig.update_layout(
        title={
            "text":"Sales Performance Dashboard",
        "x":0.5,
        "xanchor":"center"
        },
        height=850,
        template ="plotly_white",
        showlegend=False,
        paper_bgcolor="#f8f9fa",
        plot_bgcolor="white"
    )
    
    # KPI Annotations
    fig.add_annotation(
        text=f"Total Sales: {total_sales:,.0f}",
        xref="paper",yref="paper",
        x=0, y=1.15,
        showarrow=False,
        font=dict(size=14)
    )

    fig.add_annotation(
        text=f"Total Quantity: {total_quantity}",
        xref="paper", yref="paper",
        x=0.35, y=1.15,
        showarrow=False,
        font=dict(size=14)
    )

    fig.add_annotation(
        text=f"Total Customers: {total_customers}",
        xref="paper", yref="paper",
        x=0.75, y=1.15,
        showarrow=False,
        font=dict(size=14)
    )
    
    fig.write_html("final_sales_dashboard.html")



### Main Class
def main():
    df = load_data()
    total_sales, total_quantity, total_customers = calculate_kpis(df)
    monthly_sales, region_sales, product_sales = prepare_aggregations(df)

    print("KPIs:")
    print(f"Total Sales:{total_sales:,.0f}")
    print(f"Total Quantity Sold:{total_quantity}")
    print(f"Total Unique Customers:{total_customers}")

    print("Monthly Sales Preview:")
    print(monthly_sales.head())

    print("\nRegion Sales Preview:")
    print(region_sales.head())

    print("\nProduct Sales Preview:")
    print(product_sales.head())

    build_dashboard(
        df,
        monthly_sales,
        region_sales,
        product_sales,
        total_sales,
        total_quantity,
        total_customers
    )
    print(df.head())
    print("Data Loaded Successfully!")
    print("Final Dashboard Generated Successfully!")


if __name__ == "__main__":
    main()