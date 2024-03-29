#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter."""
import urllib.request
import urllib.parse
from sys import argv


def post_request(url, email):
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    order = urllib.request.Request(url, data)

    with urllib.request.urlopen(order) as response:
        order_con = response.read().decode('utf-8')
        print(f"{order_con}")


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    post_request(url, email)
