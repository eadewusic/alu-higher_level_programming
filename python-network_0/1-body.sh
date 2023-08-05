#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL using curl, and displays the body of the response if the response status code is 200.
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1"
