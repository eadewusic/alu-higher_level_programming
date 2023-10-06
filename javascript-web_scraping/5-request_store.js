#!/usr/bin/node

// Import the 'process' module to access command-line arguments
const { argv } = require('process');
const request = require('request'); // Import the 'request' module to make HTTP requests

// Make an HTTP GET request to the URL provided as the first command-line argument (argv[2])
request(argv[2], (error, response, body) => {
  if (error) {
    // If there's an error during the request, log the error to the console
    console.log(error);
    return; // Exit the script if an error occurs
  }

  const fs = require('fs'); // Import the 'fs' module to work with the file system

  // Write the response body (webpage content) to the file specified as the second command-line argument (argv[3])
  fs.writeFile(argv[3], body, (err) => {
    if (err) {
      // If there's an error while writing to the file, log the error to the console
      console.log(err);
    }
  });
});
