"""
Obtenemos los usuarios que han retuiteado un tuit.
"""
import sys
import tweepy
import credentials  # las credenciales para la conexión están aquí

if len(sys.argv) != 2:
    print("Número de argumentos erróneo", file=sys.stderr)
    sys.exit(-1)

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN, wait_on_rate_limit=True)

tweet_id = sys.argv[1]
for user in tweepy.Paginator(client.get_retweeters, id=tweet_id).flatten():
    print(user.username)
