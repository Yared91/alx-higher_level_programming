#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user as a parameter"""
import requests
from sys import argv


def post_request(letter):
    """sends post request"""
    payload = {"q": letter}
    order = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        main = order.json()
        if main == {}:
            print("No result")
        else:
            print("[{}] {}".format(main.get("id"), main.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    post_request(letter)
