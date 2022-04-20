"""
Obtenemos la línea de tiempo de un usuario. Por defecto 10 tuits.
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN)

user = client.get_user(username='daw_gc')

tweets = client.get_users_tweets(id=user.data.id, tweet_fields=['context_annotations', 'created_at', 'geo'])

n = 0
for tweet in tweets.data:
    n += 1
    print("Tuit", n, "-", tweet)
    print("------")
