#!/usr/bin/python3
"""
recursive api
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursively fetches all hot post titles
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditBot/1.0)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('data', {}).get('after', None)
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
