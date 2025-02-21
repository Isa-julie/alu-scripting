#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # If the subreddit is invalid or there is an error
    if response.status_code != 200:
        print(None)
        return
    
    # Parse the JSON response and print the titles of the top 10 posts
    posts = response.json().get('data', {}).get('children', [])
    for post in posts[:10]:
        print(post['data']['title'])
