from django.urls import path
from . import views

app_name = 'integrations'

urlpatterns = [
    path('twitter/', views.twitter_feed_view, name='twitter_feed'),
    path('facebook/', views.facebook_feed_view, name='facebook_feed'),

]
