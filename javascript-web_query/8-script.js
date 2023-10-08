#!/usr/bin/node
// This JavaScript script fetches and lists the titles for all Star Wars movies from the specified URL using jQuery.

$(document).ready(function() {
    // Define the URL to fetch the list of movies
    const apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";
  
    // Use the jQuery AJAX function to make a GET request to the URL
    $.ajax({
      url: apiUrl,
      type: "GET",
      success: function(data) {
        // Extract the movie data from the response
        const movies = data.results;
  
        // Use a loop to iterate through each movie and add its title to the list
        for (const movie of movies) {
          const title = movie.title;
          // Append the movie title as a new <li> element to the UL#list_movies
          $('#list_movies').append($('<li>').text(title));
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        // Handle errors, if any
        console.log(`Error: ${textStatus}`);
      }
    });
  });  