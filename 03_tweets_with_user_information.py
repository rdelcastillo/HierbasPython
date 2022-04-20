"""
En los ejemplos hasta ahora, hemos visto cómo obtener información de tuit para los tuits que hemos buscado. 
Sin embargo, si necesitamos información adicional asociada con el tuit, como la información del usuario que lo tuitea,
podemos usar expansiones y pasarla a la función search_recent_tweets. 

En este ejemplo, queremos información del usuario, por lo que el valor de las expansiones que pasamos es author_id. 
Además, especificaremos los campos de usuario que queremos que se devuelvan, como profile_image_url, etc. 

A partir de la respuesta, obtendremos la lista de usuarios del objeto include. Luego, buscaremos la información del 
usuario para cada tuit, utilizando el author_id del tuit.
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN)
query = '#SHS2k22 -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     user_fields=['profile_image_url'], expansions='author_id', max_results=100)

# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

n = 0
for tweet in tweets.data:
    n += 1
    user = users[tweet.author_id]
    print("Tuit", n, "de usuario:", user.username, "-", user.name, user.profile_image_url)
