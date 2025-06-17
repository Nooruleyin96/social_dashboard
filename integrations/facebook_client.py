# integrations/facebook_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")

def fetch_facebook_posts(limit=5):
    url = f"https://graph.facebook.com/{PAGE_ID}/posts"
    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "message,created_time",
        "limit": limit,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        posts = data.get("data", [])
        return posts
    except Exception as e:
        print("Error fetching Facebook posts:", e)
        return []
