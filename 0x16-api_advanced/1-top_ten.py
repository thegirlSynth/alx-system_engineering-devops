#!/usr/bin/python3
"""This module ccontains a function `top_ten`"""

import json
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "NewScript/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data").get("children")

    for post in posts[:10]:
        print(post.get("data").get("title"))
