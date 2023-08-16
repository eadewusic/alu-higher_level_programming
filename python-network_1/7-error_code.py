#!/usr/bin/python3
"""This module or script
takes a URL as a command-line argument,
sends a request to the URL,
displays the body of the response,
and prints an error message if the HTTP status code is
greater than or equal to 400.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
