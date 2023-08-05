#!/usr/bin/python3
"""This module or script
takes a URL as a command-line argument,
sends a request to the URL,
displays the body of the response (decoded in utf-8),
and manages urllib.error.HTTPError exceptions.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
