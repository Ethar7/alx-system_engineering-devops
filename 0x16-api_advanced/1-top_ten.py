#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""


import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception if status code is not 200
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except requests.RequestException:
        print(None)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
