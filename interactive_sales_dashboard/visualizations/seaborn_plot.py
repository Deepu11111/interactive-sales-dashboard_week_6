import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data.csv")
print(df.columns)
df["Date"] = pd.to_datetime(df["Date"])

sns.set_theme(style="whitegrid",palette="deep")

# Line Plot - Sales Trend

plt.figure(figsize=(10,6))
sns.lineplot(x="Date",y="Total_Sales",data=df)
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Plot - Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x="Region",y="Total_Sales",data=df)
plt.title("Sales by Region")
plt.show()

# Histogram - Sales Distribution
sns.histplot(df["Total_Sales"],kde=True)
plt.title("Sales Distribution")
plt.show()

# Scatter Plot - Sales vs Profit
sns.scatterplot(x="Quantity",y="Total_Sales",data=df)
plt.title("Sales vs Profit")
plt.show()

# Count plot - Order per region
sns.countplot(x="Region",data=df)
plt.title("Number of Orders by Region")
plt.show()

# Box Plot
sns.boxplot(x="Region",y="Total_Sales",data=df)
plt.title("Sales Distribution by Region")
plt.show()

# Violin Plot
sns.violinplot(x="Region",y="Total_Sales",data=df)
plt.title("Sales Density by Region")
plt.show()