"""
Sigue a los usuarios del fichero que le pasamos como argumento.
"""
import sys
import time

import tweepy
import credentials  # las credenciales para la conexión están aquí

DELAY = 1.5 # tiempo de espera después de cada follow

if len(sys.argv) != 2:
    print("Número de argumentos erróneo", file=sys.stderr)
    sys.exit(-1)

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN,
                       consumer_key=credentials.CONSUMER_KEY,
                       consumer_secret=credentials.CONSUMER_SECRET,
                       access_token=credentials.ACCESS_TOKEN,
                       access_token_secret=credentials.ACCESS_TOKEN_SECRET,
                       wait_on_rate_limit=True)

with open(sys.argv[1], 'r') as file_users:
    usernames = file_users.read().splitlines()

for username in usernames:
    user = client.get_user(username=username)
    if not user.errors:
        print("Siguiendo a", username)
        client.follow_user(user.data.id)
        time.sleep(DELAY)
