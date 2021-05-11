import time

mongo_db = 'twitter_stream'
collected_users_list = []
tweets_count = 0
tweets_per_user = 200
friends_per_user = 100
limit_depth = 0 
seed_names = ', '.join([])
start_time = time.time()

