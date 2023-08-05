#!/usr/bin/python3
"""This module or script
takes a URL as a command-line argument,
sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.
"""

import sys
from urllib import request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
    except Exception as e:
        print(e)
        sys.exit(1)
