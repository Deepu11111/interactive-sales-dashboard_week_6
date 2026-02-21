import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data.csv")
df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"])

# Monthly sales for clraner trend
monthly_sales = df.resample("ME",on="Date")["Total_Sales"].sum().reset_index()

# Professional theme setup
sns.set_theme(style="whitegrid",palette="deep")
plt.rcParams["figure.figsize"] = (14,10)
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 10

# 2*2 Grid

fig, axes = plt.subplots(2,2)

# Plot 1: Monthly Sales Trend
sns.lineplot(data=monthly_sales,x="Date",y="Total_Sales",marker="o",ax=axes[0,0])
axes[0,0].set_title("Monthly Sales Trend")
axes[0,0].tick_params(axis='x',rotation=45)

# Sales by region
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()
sns.barplot(data=region_sales,x="Region",y="Total_Sales",ax=axes[0,1])
axes[0,1].set_title("Total Sales by Region")

# Sales Distribution
sns.histplot(df["Total_Sales"],kde=True,ax=axes[1,0])
axes[1,0].set_title("Total Sales Distribution")

# Quantity vs Total Sales
sns.scatterplot(data=df,x="Quantity",y="Total_Sales",ax=axes[1,1])
axes[1,1].set_title("Quantity vs Total Sales")

# Final Layout Adjustments
fig.suptitle("Sales Performance Dashboard",fontsize=16,fontweight="bold")
plt.tight_layout(rect=[0,0,1,0.96])
plt.show()

print("Analysis successfull")
