#!/usr/bin/node

// Import the 'process' module to access command-line arguments
const { argv } = require('process');
const request = require('request'); // Import the 'request' module to make HTTP requests

request(argv[2], (error, response, body) => {
  if (error) {
    // If there's an error during the request, log the error
    console.log(error);
    return;
  }
  const fs = require('fs'); // Import the 'fs' module to work with the file system

  // Write the response body (webpage content) to the specified file
  fs.writeFile(argv[3], body, (err) => {
    if (err) {
      // If there's an error while writing to the file, log the error
      console.log(err);
    }
  });
});
