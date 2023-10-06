#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

const movieId = process.argv[2];

// Create the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // Parse the JSON response into a 'movieData' object
    const movieData = JSON.parse(body);

    // Extract the character URLs from the movie data
    const characterURLs = movieData.characters;

    // Create a promise to fetch character data for each URL in order
    const fetchCharacterDataInOrder = async () => {
      for (const characterURL of characterURLs) {
        const characterData = await fetchCharacterData(characterURL);
        console.log(characterData.name);
      }
    };

    // Execute the promise to fetch character data in order
    fetchCharacterDataInOrder()
      .catch((err) => console.error(`Failed to fetch character data: ${err}`));
  } else {
    console.error(error || `Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});

// Function to fetch character data and return a promise
function fetchCharacterData (characterURL) {
  return new Promise((resolve, reject) => {
    request(characterURL, (charError, charResponse, charBody) => {
      if (!charError && charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        resolve(characterData);
      } else {
        reject(charError || `Failed to fetch character data. Status code: ${charResponse.statusCode}`);
      }
    });
  });
}
