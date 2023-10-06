#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; // The API URL is the first argument passed to the script
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const characterID = '18'; // Character ID for Wedge Antilles

    // Filter the movies where Wedge Antilles is present
    const moviesWithWedge = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`));

    // Print the number of movies where Wedge Antilles is present
    console.log(moviesWithWedge.length);
  } else {
    console.error(error || `Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
