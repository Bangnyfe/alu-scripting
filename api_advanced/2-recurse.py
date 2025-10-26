#!/usr/bin/python3
"""
Module to recursively query Reddit API for all hot posts.

This module contains a recursive function to retrieve all hot article titles
from a specified subreddit using the Reddit API pagination.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query
        hot_list: List to accumulate post titles (default: [])
        after: Pagination token for the next page (default: None)

    Returns:
        List of post titles if successful, None if invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:reddit.api.project:v1.0 (by /u/yourusername)'
    }
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after_token = data.get('data', {}).get('after')

            # Add titles to hot_list
            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    hot_list.append(title)

            # If there's more data, recurse
            if after_token:
                return recurse(subreddit, hot_list, after_token)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None
