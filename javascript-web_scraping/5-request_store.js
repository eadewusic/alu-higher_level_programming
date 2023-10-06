#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');
const fs = require('fs'); // Import the 'fs' module to work with the file system

// Retrieve the URL to request from the command line arguments
const url = process.argv[2];

// Retrieve the file path to store the body response from the command line arguments
const filePath = process.argv[3];

// Make a GET request to the specified URL
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // If the request is successful (status code 200), write the response body to a file
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.error(`Error writing to the file: ${err}`);
      } else {
        console.log(`The contents of the webpage have been saved to ${filePath}`);
      }
    });
  } else {
    // Handle errors if the request fails
    console.error(error || `Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
