# run: python Code/Data_Acquisition_and_Understanding/dataPrep.py

import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import *
import numpy as np


# Define the input and output CSV file paths
input_csv = 'Sample_Data/Raw/twitter_sentiment_data.csv'
output_csv = 'Sample_Data/Processed/processed.csv'  # Output CSV file path

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

# Tokenize messages and remove stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to preprocess text: tokenize and remove stop words
def preprocess(text):
    tokens = text.lower().split()
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return filtered_tokens

# Apply preprocessing to the messages
df['tokens'] = df['message'].apply(preprocess)

# Calculate word count for each message
df['word_count'] = df['tokens'].apply(len)

# Calculate TF-IDF scores
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['message'])
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

# Create a DataFrame with TF-IDF scores
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_feature_names)

# Calculate average TF-IDF score for each message
df['average_tfidf'] = tfidf_df.mean(axis=1)


# Save the processed dataframe to a new CSV file
df.to_csv(output_csv, index=False)
print(f"Processed data saved to {output_csv}")

