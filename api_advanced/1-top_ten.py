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
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:reddit.api.project:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        data = response.json()
    except ValueError:
        return

    if not data or "data" not in data or "children" not in data["data"]:
        return

    posts = data["data"]["children"]
    if not posts:
        return

    for post in posts[:10]:
        print(post["data"].get("title"))
