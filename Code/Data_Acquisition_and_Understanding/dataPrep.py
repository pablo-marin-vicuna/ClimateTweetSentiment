import pandas as pd
from datetime import datetime

# Define the input and output CSV file paths
input_csv = '/Sample_Data/Raw/twitter_sentiment_data.csv'
output_csv = '/Sample_Data/Processed/processed.csv'  # Output CSV file path



# Function to convert tweet ID to datetime
def tweet_id_to_datetime(tweet_id):
    twitter_epoch = 1288834974657
    timestamp = (tweet_id >> 22) + twitter_epoch
    return datetime.fromtimestamp(timestamp / 1000.0)


# Load the data
df = pd.read_csv(input_csv)

# Convert tweet ID to datetime
df['datetime'] = df['tweetid'].apply(tweet_id_to_datetime)

# Extract additional features
df['date'] = df['datetime'].dt.date
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['year_month'] = df['datetime'].dt.to_period('M')
df['dayofweek'] = df['datetime'].dt.strftime('%a').str.upper()
df['message_length'] = df['message'].apply(len)


# Save the processed dataframe to a new CSV file
df.to_csv(output_csv, index=False)
print(f"Processed data saved to {output_csv}")

