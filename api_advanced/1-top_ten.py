#!/usr/bin/python3
import requests

"""
Module to fetch the top 10 hot posts from a given subreddit using Reddit's API.
This module does not follow redirects and handles invalid subreddits.
"""


def top_ten(subreddit):
    """
    Queries Reddit's API for the top 10 hot posts of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the top 10 hot posts or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/username)'}

    try:
        # Send GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Debug: Check status code of the response
        print(f"Status code: {response.status_code}")

        if response.status_code == 404:
            # Invalid subreddit, return None
            print(None)
        else:
            # Parse response and extract titles of hot posts
            data = response.json()
            if 'data' not in data or 'children' not in data['data']:
                print(None)
            else:
                posts = data['data']['children']
                for post in posts:
                    # Print the title of each post
                    print(post['data']['title'])
    except Exception as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        print(None)
