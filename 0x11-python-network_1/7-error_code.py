#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import requests
from sys import argv


def fetch_url_content(url):
    """fetches the url content"""
    try:
        order = requests.get(url)
        if order.status_code >= code:
            order.raise_for_status()
        print(f"{order.text}")
    except requests.exceptions.RequestException as e:
        new = order.status_code if hasattr(order, 'status_code') else None
        print(f"Error code: {new if new else 'Failed to connect'}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Error: Please provide URL")
    else:
        url = argv[1]
        fetch_url_content(url)
