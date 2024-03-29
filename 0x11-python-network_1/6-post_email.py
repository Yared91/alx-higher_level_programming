#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import requests
from sys import argv


def send_post_request(url, data):
    """sends a POST request with url and email"""
    order = requests.post(url, data=data)
    print(f"{order.text}")


if __name__ == "__main__":
    url = argv[1]
    main = {"email": argv[2]}
    send_post_request(url, main)
