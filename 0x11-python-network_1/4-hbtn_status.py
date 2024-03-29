#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


def get_url_response(url):
    """gets the url response"""
    order = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(order.text)}")
    print(f"\t- content: {order.text}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    get_url_response(url)
