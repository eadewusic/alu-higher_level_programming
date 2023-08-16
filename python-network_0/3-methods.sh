#!/bin/bash
# This script takes a URL as an argument, uses curl to send an HTTP OPTIONS request to the URL, and displays all the HTTP methods that the server will accept.
curl -sI "$1" | grep 'Allow:' | cut -d ' ' -f 2-
