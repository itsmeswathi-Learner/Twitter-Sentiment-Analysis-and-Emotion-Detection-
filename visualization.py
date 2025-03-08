import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_sentiment(input_file="output/sentiment_results.csv"):
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found. Run process_sentiment() first!")
        return

    df = pd.read_csv(input_file)
    sentiment_counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="coolwarm")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Analysis Results")
    
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/sentiment_plot.png")
    plt.show()
    print("✅ Sentiment visualization saved as output/sentiment_plot.png")

# Run the script
if __name__ == "__main__":
    visualize_sentiment()
