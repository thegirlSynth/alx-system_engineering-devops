#!/usr/bin/python3
"""
recurse()
"""

import json
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively queries the Reddit API and returns a list of the titles of all
    hot articles for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "NewScript/1.0"}
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    posts = response.json().get("data").get("children")

#    Append titles to hot_list for each post
    if posts:
        for post in posts:
            title = post.get("data").get("title")
            hot_list.append(title)
            print(hot_list)

        after = response.get("data").get("after")
        count += posts.get("dist")
        if after:
            return recurse(subreddit, hot_list, after, count)

    return hot_list
