# twitter-crawler
A python script the uses Twitter API to crawl through a tree of users for a specified depth to collect data that isn't bound by queries or keywords.

You can find out why I wrote this script in the first place in this [blog post](https://ahmedsamirio.github.io/Twitter-Crawler/)

## Dependencies
The script saves the data into a MondoDB database, therefore you need to have it installed. You can get it installed by following the instruction here according to your operating system <https://docs.mongodb.com/manual/installation/>

The rest of the dependencies are available in the environment.yml to create a conda environment through a terminal or an Anaconda Prompt.

```conda env create -f environment.yml```

For more info about using conda visit <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>

## Usage

First you need to insert your developer's API keys in the api_config.py file

```
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
```

Then insert the seed users (or user) you want to the search to start from and determine parameters of the search from config.py

```
mongo_db = 'twitter_stream'
collected_users_list = []
tweets_count = 0
tweets_per_user = 200
friends_per_user = 100
limit_depth = 0 
seed_names = ', '.join([])
start_time = time.time()
```

For example ```seed_names = ', '.join(['user_A_screen_name'])```

The last thing is to run the script from the terminal 

```python3 build_db.py```

The script will print updates as it collects the data with each user, each 10 users and when the the data collection is finished. The collected data will be present in specified MongoDB database whose name is set in the config.py file, and the database is created on the spot if it didn't exist before.

