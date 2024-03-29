#!/usr/bin/python3
"""requests a URL and displays the value of the variable X-Request-Id"""
import requests
from sys import argv


def get_request_id(url):
    """gets the requested id"""
    try:
        order = requests.get(url)
        main = order.headers.get('X-Request-Id')
        print(f"{main}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = argv[1]
    get_request_id(url)
