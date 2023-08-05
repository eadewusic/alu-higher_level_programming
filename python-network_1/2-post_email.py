#!/usr/bin/python3
"""This module or script
takes a URL and an email as command-line arguments,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    try:
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except Exception as e:
        print(e)
        sys.exit(1)
