#!/usr/bin/python3
"""requests a URL and displays the value of the X-Request-Id variable"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    order = urllib.request.Request(argv[1])
    with urllib.request.urlopen(order) as response:
        headers = dict(response.headers)
        main = headers.get("X-Request-Id")
        print(main)
