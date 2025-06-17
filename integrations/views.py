from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .twitter_client import fetch_recent_tweets

from django.core.cache import cache

# def twitter_feed_view(request):
#     tweets = cache.get('twitter_feed')
#     if not tweets:
#         tweets = fetch_recent_tweets(username='musharrafaleem')
#         cache.set('twitter_feed', tweets, timeout=300)  # cache for 5 minutes
#     return render(request, 'integrations/twitter_feed.html', {'tweets': tweets})

def twitter_feed_view(request):
    user = request.user

    # Get username from CustomUser or related UserProfile
    twitter_username = getattr(user, 'twitter_username', None)

    # Or if you're using a UserProfile model:
    # twitter_username = getattr(user.profile, 'twitter_username', None)

    if not twitter_username:
        return render(request, 'integrations/twitter_feed.html', {
            'error': "No Twitter username set in your profile."
        })

    cache_key = f'twitter_feed_{twitter_username}'
    tweets = cache.get(cache_key)

    if not tweets:
        tweets = fetch_recent_tweets(username=twitter_username)
        cache.set(cache_key, tweets, timeout=300)  # 5 min cache

    return render(request, 'integrations/twitter_feed.html', {'tweets': tweets})


# integrations/views.py
from .facebook_client import fetch_facebook_posts

def facebook_feed_view(request):
    posts = fetch_facebook_posts()
    return render(request, 'integrations/facebook_feed.html', {'posts': posts})


