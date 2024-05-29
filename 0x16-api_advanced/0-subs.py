#!/usr/bin/python3
"""
0-main
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    geting_inf = requests.get(subreddit_url, headers=headers)

    if geting_inf.status_code == 404:
        return 0

    data = geting_inf.json()
    subscribe = data.get('data').get('subscribers')
    return subscribe
