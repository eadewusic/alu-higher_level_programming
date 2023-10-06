#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

// Create the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);

    // Extract the character URLs from the movie data
    const characterURLs = movieData.characters;

    // Iterate through the character URLs and fetch the character names
    characterURLs.forEach((characterURL) => {
      request(characterURL, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error(charError || `Failed to fetch character data. Status code: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.error(error || `Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});
