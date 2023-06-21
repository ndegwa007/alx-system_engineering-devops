#!/usr/bin/python3
"""query - the Reddit API using recursion"""

import requests


def recurse(subreddit, after=None, hot_topics=[]):
    """ query all hot topics from subreddit """

    # base case
    if hot_topics is None:
        return []

    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'super-bot/1.2'}
    params = {'limit': 100}

    if after:
        params['after'] = after
    try:
        response = requests.get(base_url, params=params, headers=headers)
    except Exception as e:
        print(f"An error occurred during the API request: {e}")

    # get json data
    try:
        data = response.json()['data']
    except Exception as e:
        print(f"KeyError: {e}")

    for child in data['children']:
        hot_topics.append(child['data']['title'])

    if data['after'] is not None:
        recurse(subreddit, data['after'], hot_topics)
    return hot_topics
