import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os
from collections import Counter

def visualize_sentiment(input_file="output/sentiment_results.csv"):
    """ Generate a Bar Chart and Pie Chart for sentiment distribution """
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run sentiment analysis first!")
        return

    df = pd.read_csv(input_file)
    sentiment_counts = df["Sentiment"].value_counts()

    # Bar Chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Analysis Results")
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/sentiment_bar_chart.png")
    plt.show()
    print("✅ Sentiment bar chart saved as output/sentiment_bar_chart.png")

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=["green", "red", "gray"])
    plt.title("Sentiment Distribution")
    plt.savefig("output/sentiment_pie_chart.png")
    plt.show()
    print("✅ Sentiment pie chart saved as output/sentiment_pie_chart.png")

def generate_wordcloud(input_file="output/cleaned_tweets.csv"):
    """ Generate a Word Cloud from cleaned tweets """
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run preprocessing first!")
        return

    df = pd.read_csv(input_file)
    text = " ".join(tweet for tweet in df["Cleaned_Tweet"].dropna())

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Tweets")
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/wordcloud.png")
    plt.show()
    print("✅ Word Cloud saved as output/wordcloud.png")

def word_frequency(input_file="output/cleaned_tweets.csv"):
    """ Generate a CSV file with word frequency count """
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run preprocessing first!")
        return

    df = pd.read_csv(input_file)
    words = " ".join(tweet for tweet in df["Cleaned_Tweet"].dropna()).split()
    word_counts = Counter(words)

    df_word_freq = pd.DataFrame(word_counts.items(), columns=["Word", "Count"]).sort_values(by="Count", ascending=False)
    df_word_freq.to_csv("output/word_frequency.csv", index=False)
    print("✅ Word Frequency Count saved as output/word_frequency.csv")

# Run all visualization functions
if __name__ == "__main__":
    visualize_sentiment()   # Generate Bar Chart & Pie Chart
    generate_wordcloud()    # Generate Word Cloud
    word_frequency()        # Generate Word Frequency CSV
