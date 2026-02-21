import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("../data/sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"]=(10,8)

# Correlation matrix (Numerical Only)
numeric_df = df[["Quantity","Price","Total_Sales"]]

correlation = numeric_df.corr()
plt.figure()

sns.heatmap(correlation,annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5)

plt.title("Correlation Matrix - Sales Data",fontsize=14)
plt.tight_layout()
plt.show()

# Region vs Product Sales Heatmap
pivot_table = df.pivot_table(values="Total_Sales",index="Region",columns="Product",aggfunc="sum")

plt.figure(figsize=(12,8))

sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt=".0f",linewidths=0.5)

plt.title("Total Sales by Region and Product",fontsize=14)
plt.tight_layout()
plt.show()

print("sales analysis completed")


