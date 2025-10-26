#!/usr/bin/python3
"""
Module to query Reddit API for hot posts.

This module contains a function to retrieve and display the titles
of the top 10 hot posts from a specified subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'linux:reddit.api.project:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    if 'data' not in data:
        print(None)
        return

    data_dict = data.get('data')
    if not data_dict or 'children' not in data_dict:
        print(None)
        return

    posts = data_dict.get('children')
    if not posts:
        print(None)
        return

    count = 0
    for post in posts:
        if count >= 10:
            break
        post_data = post.get('data', {})
        title = post_data.get('title')
        if title:
            print(title)
            count += 1
