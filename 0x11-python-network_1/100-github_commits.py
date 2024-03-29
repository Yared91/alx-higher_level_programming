#!/usr/bin/python3
"""interview time"""
import requests
from sys import argv


def github_commits(owner, repo):
    """gets the github commits"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    main = requests.get(url)
    orders = main.json()

    for order in orders[:10]:
        new = order.get("new")
        author_name = order.get("commit").get("author").get("name")
        print(f"{new}: {author_name}")


if __name__ == "__main__":
    if len(argv) < 3:
        print("Please provide owner and repo as command line arguments.")
    else:
        repo = argv[1]
        owner = argv[2]
    github_commits(owner, repo)
