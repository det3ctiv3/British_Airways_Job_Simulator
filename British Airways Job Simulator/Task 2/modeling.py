import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with specified encoding
df = pd.read_csv("customer_booking.csv", encoding="latin1")

# Relevant columns for customer preferences
relevant_columns = ["sales_channel", "trip_type", "wants_extra_baggage", "wants_preferred_seat",
                    "wants_in_flight_meals", "flight_day", "route", "booking_origin"]

# Explore unique values and frequencies
for column in relevant_columns:
    print(f"Column: {column}")
    print(df[column].value_counts())
    print()

# Visualize preferences
for column in relevant_columns:
    plt.figure(figsize=(8, 6))
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f"Customer Preferences - {column}")
    plt.xlabel("Preference")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.savefig(f"{column}_preference.png", bbox_inches='tight')
    plt.show()
