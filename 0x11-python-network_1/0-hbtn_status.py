#!/usr/bin/python3
"""Writes a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


def fetch_status():
    """fetches https://alx-intranet.hbtn.io/status"""
    try:
        order = urllib.request.Request("https://alx-intranet.hbtn.io/status")
        with urllib.request.urlopen(order) as response:
            main = response.read()
            print("Body response:")
            print(f"\t- type: {type(main)}")
            print(f"\t- content: {main}")
            print(f"\t- utf8 content: {main.decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_status()
