import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Data
df = pd.read_csv("../data/sales_data.csv")

# professional theme
sns.set_theme(style = "whitegrid",palette="deep")

plt.figure(figsize=(8,6))
sns.boxplot(x="Region",y="Total_Sales",data=df)

plt.title("Sales Distribution by Region")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("../outputs/boxplot.png")
plt.show()

# 2.Correlation Heatmap
plt.figure(figsize=(10,8))
correlation = df.corr(numeric_only=True)

sns.heatmap(correlation,annot=True,cmap="coolwarm", fmt=".2f",linewidths=0.5)
    
plt.title("Correlation Matrix")
plt.tight_layout()

plt.savefig("../outputs/heatmap.png")

plt.show()

# 3.Multiple Subplots in one fig
fig,axes= plt.subplots(2, 2, figsize=(14,10))

# Sales by region 
sns.barplot(x="Region",y="Total_Sales",data=df ,ax=axes[0,0])
axes[0,0].set_title("Sales by Region")


# Sales Trend
sns.lineplot(x="Date" , y="Total_Sales",data=df ,ax=axes[0,1])
axes[0,1].set_title("Sales Over Time")

# Quantity Distribution
sns.histplot(df["Quantity"],kde=True,ax=axes[1,0])
axes[1,0].set_title("Quantity Distribution")

# Profit vs sales (if there is any existance)
if "Profit" in df.columns:
    sns.scatterplot(x="Total_Sales",y="Profit",data=df , ax=axes[1,1])
    axes[1,1].set_title("Sales vs Profit")

plt.tight_layout()
plt.show()