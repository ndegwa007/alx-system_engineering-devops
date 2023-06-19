#!/usr/bin/python3
"""query - the Reddit API using recursion"""

import requests


def recurse(subreddit, hot_post=[]):
    """ query all hot topics from subreddit """
    headers = {'User-Agent': 'super-bot/1.2'}
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        posts = response_json['data']['children']
                
