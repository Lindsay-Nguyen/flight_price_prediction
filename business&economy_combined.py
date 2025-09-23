import pandas as pd

# Load cleaned datasets
biz_cleaned = pd.read_csv("business_cleaned1.csv")
eco_cleaned = pd.read_csv("economy_cleaned1.csv")

# Add class labels (if missing)
if "class" not in biz_cleaned.columns:
    biz_cleaned["class"] = "Business"

if "class" not in eco_cleaned.columns:
    eco_cleaned["class"] = "Economy"

# Combine them
df = pd.concat([biz_cleaned, eco_cleaned], ignore_index=True)

# Save final dataset for ML
output_path = "combined_class.csv"
df.to_csv(output_path, index=False)

print("✅ Combined dataset saved as:", output_path)
print("Shape:", df.shape)
print(df.head())
