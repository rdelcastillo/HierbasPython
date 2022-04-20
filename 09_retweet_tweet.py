"""
Crear un tuit.
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

client = tweepy.Client(consumer_key=credentials.CONSUMER_KEY,
                       consumer_secret=credentials.CONSUMER_SECRET,
                       access_token=credentials.ACCESS_TOKEN,
                       access_token_secret=credentials.ACCESS_TOKEN_SECRET)

response = client.retweet(1516822274762018825)
print(response)