#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user as a parameter"""
import requests
from sys import argv


def post_request(url):
    """sends post request"""
    top = {"q": url}
    order = requests.post("http://0.0.0.0:5000/search_user", data=top)

    try:
        main = order.json()
        if main == {}:
            print(f{"No result"})
        else:
            print("[{}] {}".format(main.get("id"), main.get("name")))
    except ValueError:
        print(f{"Not a valid JSON"})


if __name__ == "__main__":
    if len(argv) == 1:
        url = ""
    else:
        url = argv[1]
    post_request(url)
