#!/usr/bin/python3
"""This module or script
takes a URL and an email address as command-line arguments,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
