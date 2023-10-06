#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2]; // The movie ID is the first argument passed to the script
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error(error || `Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
