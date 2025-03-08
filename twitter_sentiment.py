import tweepy
import os
import pandas as pd
from dotenv import load_dotenv

# Load API credentials from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to fetch tweets
def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(count)
    tweet_data = [[tweet.full_text] for tweet in tweets]
    df = pd.DataFrame(tweet_data, columns=["Tweet"])
    df.to_csv("output/tweets.csv", index=False)
    print(f"✅ Fetched {len(df)} tweets for '{keyword}' and saved to output/tweets.csv")
    return df

# Run the script
if __name__ == "__main__":
    keyword = input("Enter a keyword to search tweets: ")
    fetch_tweets(keyword, 100)
