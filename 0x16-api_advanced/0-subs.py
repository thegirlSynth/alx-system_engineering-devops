#!/usr/bin/python3
"""This module ccontains a function `number_of_subscribers`"""

import json
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "NewScript/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    subscribers = response.json().get("data").get("subscribers")

    return int(subscribers)
