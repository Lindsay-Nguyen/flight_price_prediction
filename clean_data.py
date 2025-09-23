import pandas as pd
import re

def clean_flight_data(df, flight_class):
    # Add class column
    df["class"] = flight_class

    # Clean price
    df["price"] = df["price"].astype(str).str.replace(",", "").astype(int)

    # Convert time_taken into decimal hours
    def time_to_hours(x):
        h, m = 0, 0
        h_match = re.search(r"(\d+)h", str(x))
        m_match = re.search(r"(\d+)m", str(x))
        if h_match:
            h = int(h_match.group(1))
        if m_match:
            m = int(m_match.group(1))
        return round(h + m/60, 2)

    df["duration"] = df["time_taken"].apply(time_to_hours)

    # Rename columns
    df = df.rename(columns={
        "from": "source_city",
        "to": "destination_city",
        "dep_time": "departure_time",
        "arr_time": "arrival_time",
        "num_code": "flight"
    })

    # Bucket times into categories
    def bucket_time(t):
        try:
            hour = int(str(t).split(":")[0])
        except:
            return "Unknown"
        if 5 <= hour < 8: return "Early_Morning"
        elif 8 <= hour < 12: return "Morning"
        elif 12 <= hour < 16: return "Afternoon"
        elif 16 <= hour < 20: return "Evening"
        else: return "Night"

    df["departure_time"] = df["departure_time"].apply(bucket_time)
    df["arrival_time"] = df["arrival_time"].apply(bucket_time)

    # Add days_left if missing
    if "days_left" not in df.columns:
        df["days_left"] = 1

    # Select final columns
    df = df[[
        "airline", "flight", "source_city", "departure_time", "stop",
        "arrival_time", "destination_city", "class", "duration", "days_left", "price"
    ]]

    return df


# === Example Usage ===
biz = pd.read_csv("C:\\Users\\realm\\OneDrive\\Documents\\Thuy One Drive\\OneDrive\\data_job_projects\\flight_prediction_handlingdataset\\original_dataset\\business_cleaned.csv")
eco = pd.read_csv("C:\\Users\\realm\\OneDrive\\Documents\\Thuy One Drive\\OneDrive\\data_job_projects\\flight_prediction_handlingdataset\\original_dataset\\economy_cleaned.csv")

biz_cleaned = clean_flight_data(biz, "Business")
eco_cleaned = clean_flight_data(eco, "Economy")

biz_cleaned.to_csv("business_cleaned1.csv", index=False)
eco_cleaned.to_csv("economy_cleaned1.csv", index=False)

print("✅ Cleaned datasets saved: business_cleaned1.csv, economy_cleaned1.csv")
