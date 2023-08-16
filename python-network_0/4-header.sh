#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL with a custom header, and displays the body of the response.
curl -s -i "$1" | grep -E "HTTP" | cut --delimiter=" " -f 3 | tr -d '\r\n'
