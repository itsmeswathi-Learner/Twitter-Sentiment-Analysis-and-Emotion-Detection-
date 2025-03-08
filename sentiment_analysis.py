from textblob import TextBlob
import pandas as pd
import os

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return sentiment

def process_sentiment(input_file="output/cleaned_tweets.csv", output_file="output/sentiment_results.csv"):
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run preprocess_csv() first!")
        return

    df = pd.read_csv(input_file)

    # 🔥 Fix: Convert NaN values to an empty string before sentiment analysis
    df["Cleaned_Tweet"] = df["Cleaned_Tweet"].fillna("")

    df["Sentiment"] = df["Cleaned_Tweet"].apply(analyze_sentiment)
    df.to_csv(output_file, index=False)
    print(f"✅ Sentiment analysis completed. Results saved to {output_file}")

# Run the script
if __name__ == "__main__":
    process_sentiment()
