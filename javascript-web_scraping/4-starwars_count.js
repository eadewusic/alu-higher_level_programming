#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Retrieve the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API using the provided URL
request(apiUrl, function (error, response, body) {
  if (!error) {
    // Parse the response body as JSON
    const results = JSON.parse(body).results;

    // Count the number of movies where 'Wedge Antilles' is present
    const count = results.reduce((count, movie) => {
      // Check if any character's URL ends with '/18/' (the ID for 'Wedge Antilles')
      if (movie.characters.find((character) => character.endsWith('/18/'))) {
        return count + 1; // Increment the count if 'Wedge Antilles' is found in the movie
      }
      return count; // Otherwise, keep the count unchanged
    }, 0);

    // Print the count to the console
    console.log(count);
  } else {
    // Handle errors if the request fails
    console.error(error || `Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
