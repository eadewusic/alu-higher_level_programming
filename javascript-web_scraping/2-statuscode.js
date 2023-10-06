#!/usr/bin/node

const request = require('request');
const url = process.argv[2]; // The URL to request (GET) is the first argument passed to the script
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
