import tweepy
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# Get Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
# Twitter API v2 uses Bearer Token
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Authenticate with v2 API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_recent_tweets(username, count=10):
    try:
        # Get user ID from username
        user = client.get_user(username=username)
        user_id = user.data.id

        # Fetch recent tweets using v2 endpoint
        tweets = client.get_users_tweets(id=user_id, max_results=count, tweet_fields=['created_at'])

        # Return tweet content and creation time
        return [{"text": t.text, "created_at": t.created_at} for t in tweets.data] if tweets.data else []
    except Exception as e:
        print("Error fetching tweets:", e)
        return []

