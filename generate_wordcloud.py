import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

def generate_wordcloud(input_file="output/cleaned_tweets.csv"):
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run preprocess_csv() first!")
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

# Run the script
if __name__ == "__main__":
    generate_wordcloud()
