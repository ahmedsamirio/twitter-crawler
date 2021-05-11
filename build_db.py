import time
import sys
from twitter_api import *
from config import *

if __name__ == "__main__":

    twitter_api = oauth_login()

    print("Collecting users and tweets...\n", file=sys.stderr)
    
    seed_users = collect_users(twitter_api, seed_names)

    for user in seed_users:
        collected_users, tweets_count, seconds = stream_from_users(twitter_api, user, tweets_per_user, friends_per_user, mongo_db, 0)

    print("Data collection finished.")
    print("Collected users: %d user\nCollected tweets: %d tweet\nDuration: %d seconds" %
              (collected_users, tweets_count, seconds), "\n", file=sys.stderr)