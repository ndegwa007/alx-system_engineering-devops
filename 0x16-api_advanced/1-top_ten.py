#!/usr/bin/python3

"""
model queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """ titles of the first 10 hot posts for a subreddit """
    headers = {'User-Agent': 'super-bot/1.1'}
    count = 9
    response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit={count}",
            headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        posts = response_json['data']['children']
        p = [post['data']['title'] for post in posts]
        for title in p:
            print(title)
    else:
        print("None")
