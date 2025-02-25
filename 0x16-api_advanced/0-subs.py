#!/usr/bin/python3
"""
return number of subscribers from reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    return number of subscribers or 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom-Reddit-Subscriber-Checker/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
