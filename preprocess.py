import os
import re
import pandas as pd

# Function to clean tweets
def clean_tweet(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = re.sub(r"\@\w+|\#", "", text)  # Remove mentions & hashtags
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase and trim spaces
    return text

# Function to preprocess tweets
def preprocess_csv(input_file="output/tweets.csv", output_file="output/cleaned_tweets.csv"):
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run fetch_tweets_v2() first!")
        return
    
    df = pd.read_csv(input_file)
    df["Cleaned_Tweet"] = df["Tweet"].apply(clean_tweet)
    df.to_csv(output_file, index=False)
    print(f"✅ Preprocessed tweets saved to {output_file}")

# Run the script
if __name__ == "__main__":
    preprocess_csv()
