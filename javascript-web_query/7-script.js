#!/usr/bin/node
// This JavaScript script fetches the character name from the specified URL and displays it in DIV#character using jQuery.

$(document).ready(function() {
    // Define the URL to fetch the character data
    const apiUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
  
    // Use the jQuery AJAX function to make a GET request to the URL
    $.ajax({
      url: apiUrl,
      type: "GET",
      success: function(data) {
        // Extract the character name from the response data
        const characterName = data.name;
  
        // Display the character name in the DIV#character
        $('#character').text(characterName);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        // Handle errors, if any
        console.log(`Error: ${textStatus}`);
      }
    });
  });  