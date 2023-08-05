#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL with a custom header, and displays the body of the response.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
