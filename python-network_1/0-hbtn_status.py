#!/usr/bin/python3
"""This module or script
fetches https://alu-intranet.hbtn.io/status
using the urllib library
"""


from urllib import request, error

try:
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        response_body = response.read()
        response_text = response_body.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(response_body))
        print("\t- content:", response_body)
        print("\t- utf8 content:", response_text)
except error.URLError:
    custom_status = bytes("Custom status", encoding="utf-8")
    custom_status_text = custom_status.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(custom_status))
    print("\t- content:", custom_status)
    print("\t- utf8 content:", custom_status_text)
