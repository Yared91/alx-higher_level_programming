#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import urllib.request
import urllib.error
from sys import argv


def fetch_url_content(url):
    """fetches the url content"""
    order = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(order) as response:
            main = response.read().decode('utf-8')
            print(f"{main}")
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    url = argv[1]
    fetch_url_content(url)
