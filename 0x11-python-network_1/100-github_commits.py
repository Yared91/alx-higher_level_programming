#!/usr/bin/python3
"""interview time"""
import requests
from sys import argv


def github_commits(owner, repo):
    """gets the github commits"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    main = requests.get(url)
    commits = main.json()

    for commit in commits[:10]:
        new = commit.get("new")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{new}: {author_name}")


if __name__ == "__main__":
    if len(argv) < 3:
        print("Please provide owner and repo as command line arguments.")
    else:
        owner = argv[2]
        repo = argv[1]
    github_commits(owner, repo)
