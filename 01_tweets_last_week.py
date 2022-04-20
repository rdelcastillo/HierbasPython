"""
Buscamos los tuits (no RT) de los últimos siete días. v2.

Para buscar Tweets de los últimos 7 días usamos la función 'search_recent_tweets' disponible en Tweepy a la que hay
que pasar una consulta (query) para especificar los datos de búsqueda.

Estamos excluyendo los retweets usando '-is:retweet'. De manera predeterminada solo obtenemos el ID del tuit y su texto.
Si necesitamos más campos adicionales como 'context_annotations', 'created_at' (la hora en que se creó el tweet), etc.,
se pueden especificar utilizando el parámetro 'tweet_fields'.

De forma predeterminada, una solicitud devuelve 10 tuits, si queremos más hay que especificarlo usando el parámetro
'max_results' (máximo 100).

No todos los tuits tienen 'contexts_annotations'' asociadas, por lo que, en este ejemplo solo las mostramos si están
disponibles para un tuit.
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN)
query = 'from:' + credentials.TWITTER_USER + ' -is:retweet'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

n = 0
for tweet in tweets.data:
    n += 1
    print('Tuit nº', n, 'con tweet_id:', tweet.id, 'creado el', tweet.created_at.strftime('%d/%m/%Y - %H:%M:%S'))
    print('Texto:', tweet.text)
    if len(tweet.context_annotations) > 0:
        print('Contexto:', tweet.context_annotations)
    print("------")
