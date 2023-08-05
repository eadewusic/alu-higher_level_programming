#!/usr/bin/python3
"""This module or script
uses the requests package
to fetch https://alu-intranet.hbtn.io/status
and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
