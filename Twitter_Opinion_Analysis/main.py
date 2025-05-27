import tweepy
from textblob import TextBlob
import time

BEARER_TOKEN = 'Your Bearer Token'

client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_tweets(keyword, max_tweets=50):
    query = f"{keyword} -is:retweet lang:en"
    sentiment_count = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    tweets_analyzed = 0

    try:
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['text'], max_results=10).flatten(limit=max_tweets):
            sentiment = get_sentiment(tweet.text)
            sentiment_count[sentiment] += 1
            tweets_analyzed += 1
            print(f"[{sentiment}] {tweet.text}\n")
    except tweepy.TooManyRequests:
        print("Rate limit reached. Waiting before retrying...")
        time.sleep(900)  
    except Exception as e:
        print("Error:", e)

    print("\nSentiment Summary:")
    print(sentiment_count)
    print(f"Total Tweets Analyzed: {tweets_analyzed}")

if __name__ == "__main__":
    keyword = input("Enter a keyword to analyze: ")
    analyze_tweets(keyword)
