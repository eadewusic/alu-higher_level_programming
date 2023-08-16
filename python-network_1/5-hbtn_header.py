#!/usr/bin/python3
"""This module or script
takes a URL as a command-line argument,
sends a request to the URL,
and displays the value of the X-Request-Id variable
in the response header.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
