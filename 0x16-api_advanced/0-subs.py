#!/usr/bin/python3
"""queries the reddit API"""
import json
import requests


def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'super-bot/1.0'}
    response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        if 'subscribers' in response_json['data']:
            return response_json['data']['subscribers']
    return 0
