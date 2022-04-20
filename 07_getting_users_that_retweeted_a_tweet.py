"""
Obtenemos los usuarios que han retuiteado un tuit.
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN)

tweet_id = '1515297033816616963'
tweet = client.get_tweet(tweet_id)
print(tweet.data.text)

users = client.get_retweeters(id=tweet_id, max_results=100)

print('Usuarios que retuitearon el tuit id', tweet_id)
n = 0
for user in users.data:
    n += 1
    print(n, '- @' + user.username, '/', user.name)
