#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL using curl, and displays the body of the response if the response status code is 200.
curl -s -L -I "$1" -w "%{http_code}" | grep "200" -q && curl -sL "$1"
