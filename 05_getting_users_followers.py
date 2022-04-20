"""
Obtenemos los seguidores de un usuario (máximo 1000).
"""

import tweepy
import credentials  # las credenciales para la conexión están aquí

client = tweepy.Client(bearer_token=credentials.BEARER_TOKEN)

user = client.get_user(username='daw_gc')
users = client.get_users_followers(id=user.data.id, max_results=1000)

n = 0
for user in users.data:
    n += 1
    print(n, '- @' + user.username, '/', user.name)
