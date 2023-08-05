#!/usr/bin/python3
"""This module or script
takes a letter as a command-line argument,
sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter,
and handles JSON responses accordingly.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        json_response = response.json()
        if isinstance(json_response, dict) and 'id' in json_response and 'name' in json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
