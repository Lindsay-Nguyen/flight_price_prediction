import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load cleaned dataset
df = pd.read_csv(
    r"C:/Users/realm/OneDrive/Documents/Thuy One Drive/OneDrive/data_job_projects/flight_prediction_handlingdataset/original_dataset/business_cleaned.csv"
)

# Clean 'price' column to numeric
df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(",", "", regex=False)   # remove commas
    .str.replace("$", "", regex=False)   # remove dollar signs
    .str.strip()
)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Drop rows with missing/invalid prices
df = df.dropna(subset=["price"])

# ==========================
# 1️⃣ Average flight price by airline (bar chart)
# ==========================
plt.figure(figsize=(12,6))
avg_price = df.groupby("airline")["price"].mean().sort_values()
sns.barplot(x=avg_price.index, y=avg_price.values, palette="viridis")

plt.title("Average Flight Price by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Price")

# Add labels
for i, v in enumerate(avg_price.values):
    plt.text(i, v, f"{v:.0f}", ha="center", va="bottom", fontsize=8)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart1_avg_price_by_airline.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================
# 2️⃣ Price distribution (histogram)
# ==========================
plt.figure(figsize=(10,6))
sns.histplot(df["price"], bins=50, kde=True, color="blue")

plt.title("Distribution of Flight Prices")
plt.xlabel("Price")
plt.ylabel("Number of Flights")
plt.tight_layout()
plt.savefig("chart2_price_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================
# 3️⃣ Effect of stops on price (boxplot)
# ==========================
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="stop", y="price", palette="Set2")

plt.title("Effect of Number of Stops on Flight Price")
plt.xlabel("Stops")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("chart3_effect_of_stops.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================
# 4️⃣ Cheapest vs most expensive routes
# ==========================
route_prices = (
    df.groupby(["source", "destination"])["price"]
    .agg(["min", "max"])
    .reset_index()
)

# Melt for plotting
route_prices_melted = route_prices.melt(
    id_vars=["source", "destination"],
    value_vars=["min", "max"],
    var_name="Type",
    value_name="Price"
)

plt.figure(figsize=(14,7))
sns.barplot(
    data=route_prices_melted,
    x="source",
    y="Price",
    hue="Type",
    palette="coolwarm"
)

plt.title("Cheapest vs Most Expensive Routes (by Source)")
plt.xlabel("Source City")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart4_cheapest_vs_expensive_routes.png", dpi=300, bbox_inches="tight")
plt.show()

