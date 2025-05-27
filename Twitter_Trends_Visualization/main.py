import tweepy
from collections import Counter

consumer_key = 'Enter your consumer key'
consumer_secret = 'Enter your consumer secret'
access_token = 'Enter your access token'
access_token_secret = 'Enter your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_trending_topics():
    try:
        trends = api.trends_place(1)  
        trends_list = trends[0]["trends"]
        
        trending_hashtags = []
        for trend in trends_list:
            trending_hashtags.append(trend["name"])
        
        return trending_hashtags
    except Exception as e:
        print(f"Error fetching trends: {e}")
        return []

def fetch_tweets(trends):
    tweets = []
    
    for trend in trends:
        for tweet in tweepy.Cursor(api.search, q=trend, lang="en", rpp=10).items(10):
            tweets.append(tweet.text)
    
    return tweets

def analyze_tweets(tweets):
    combined_text = ' '.join(tweets)
    
    words = combined_text.split()
    word_count = Counter(words)
    
    print("Most Common Words in Trending Tweets:")
    for word, count in word_count.most_common(10):
        print(f"{word}: {count}")

def main():
    print("Fetching trending topics...")
    trends = get_trending_topics()
    
    if not trends:
        print("No trending topics found. Exiting.")
        return
    
    print("Trending Hashtags:", trends)
    
    print("Fetching tweets...")
    tweets = fetch_tweets(trends)
    
    print("Analyzing tweets...")
    analyze_tweets(tweets)

if __name__ == "__main__":
    main()
