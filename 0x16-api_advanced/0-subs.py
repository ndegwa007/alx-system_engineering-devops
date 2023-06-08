#!/usr/bin/python3
"""model - working with reddit api"""

import requests


def number_of_subscribers(subreddit):
    """ a function to get the number of subscribers of a subreddit"""
    headers = {"User-Agent": 'my_bot/0.0.1'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
