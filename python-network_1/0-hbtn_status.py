#!/usr/bin/python3
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".format(utf8_content))
