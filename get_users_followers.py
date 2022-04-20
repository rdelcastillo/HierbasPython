"""
Obtenemos los seguidores del usuario que pasamos como parámetro.
"""
import sys
import tweepy
import credentials  # las credenciales para la conexión están aquí

if len(sys.argv) != 2:
    print("Número de argumentos erróneo", file=sys.stderr)
    sys.exit(-1)

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN, wait_on_rate_limit=True)

user_query = client.get_user(username=sys.argv[1])
for user in tweepy.Paginator(client.get_users_followers, id=user_query.data.id, max_results=1000).flatten():
    print(user.username)
