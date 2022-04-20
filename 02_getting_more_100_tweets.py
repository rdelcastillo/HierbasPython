"""
Si necesitamos más de 100 tuits hay que usar el paginador y especificar la cantidad total deseada.
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

LIMIT = 500

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN)
query = '#SHS2k22 -is:retweet'

n = 0
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=LIMIT):
    n += 1
    print('Tuit nº', n, 'con tweet_id:', tweet.id, 'creado el', tweet.created_at.strftime('%d/%m/%Y - %H:%M:%S'))
    print('Texto:', tweet.text)
    if len(tweet.context_annotations) > 0:
        print('Contexto:', tweet.context_annotations)
    print("------")
