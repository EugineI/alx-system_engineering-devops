#!/usr/bin/python3
"""
prints titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    prints first ten titles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom-Reddit-TopTen-Checker/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
