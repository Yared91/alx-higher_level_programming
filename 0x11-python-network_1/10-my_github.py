#!/usr/bin/python3
""" uses the GitHub API to display your id"""
import requests
from sys import argv
from sys import exit
from requests.auth import HTTPBasicAuth


def get_github_id(username, password):
    """uses the GitHub API to display your id"""
    auth = HTTPBasicAuth(username, password)
    order = requests.get("https://api.github.com/user", auth=auth)
    if order.status_code == 200:
        print(order.json().get("id"))
    else:
        print(f"Failed to retrieve GitHub ID. Status code: {order.status_code}")


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./10-my_github.py <GitHub username> <GitHub password>")
    else:
        username = argv[1]
        password = argv[2]
    get_github_id(username, password)
