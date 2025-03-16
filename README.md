# 🐦 Twitter Sentiment Analysis & Emotion Detection  

This project performs **sentiment analysis** and **emotion detection** on real-time **Twitter data** using **Natural Language Processing (NLP)** and **Machine Learning (ML)** models. It helps in understanding the overall sentiment of tweets (**positive, negative, or neutral**) and detects emotions based on the text content.  


## 📌 **Project Features**:

✅ **Fetches live tweets** using **Twitter API v2 (Free Access)**  
✅ **Preprocesses tweets** (removes URLs, emojis, mentions, hashtags, etc.)  
✅ **Performs sentiment analysis** using **TextBlob**  
✅ **Generates visual insights** (Bar Charts, Pie Charts, Word Clouds)  
✅ **Monitors real-time sentiment trends** for brands or keywords  


## 🛠 **Technologies Used**:

- **Python 3.13**  
- **Tweepy (Twitter API v2)**  
- **TextBlob** for sentiment analysis  
- **Pandas, NumPy** for data handling  
- **Matplotlib, Seaborn** for visualization  
- **WordCloud** for generating word clouds  


## 🔑 **Set Up Twitter API Keys**
To fetch tweets, you need **Twitter Developer API Keys**.  

1️⃣ **Sign up at** [developer.twitter.com](https://developer.twitter.com/)  
2️⃣ **Get API keys & access tokens**, then create a `.env` file in your project folder:  

API_KEY=your_api_key

API_SECRET=your_api_secret

ACCESS_TOKEN=your_access_token

ACCESS_SECRET=your_access_secret

BEARER_TOKEN=your_bearer_token

⚡ Twitter API Access (Free Tier)
This project uses Twitter API v2 (Free Access) to fetch live tweets.
📌 Limitations of Free Access:

Can only fetch tweets from the last 7 days.
Rate limit: 450 requests per 15 minutes for recent searches.
Twitter resets free-tier limits every 15 minutes to 1 hour.
No access to historical tweets (for older data, paid plans are required).

📢 Want more access? Upgrade to a Twitter Developer Premium/Enterprise plan at developer.twitter.com

📊 Results & Visualizations:

1️⃣ Sentiment Distribution (Bar Chart)

 ![image](https://github.com/user-attachments/assets/f4a5d22f-50a4-4909-8579-1505c74f99f6)


2️⃣ Sentiment Distribution (Pie Chart)

![image](https://github.com/user-attachments/assets/d7e36c2b-7b68-4af5-8db3-38220e8bfa0c)


3️⃣ Word Cloud of Most Used Words

![image](https://github.com/user-attachments/assets/da3b975b-292f-4084-95a1-43f1a471a449)


4️⃣ Word Frequency Table

Check output/word_frequency.csv for the most common words in the dataset.
