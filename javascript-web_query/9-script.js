#!/usr/bin/node
// This JavaScript script fetches the translation of "hello" from the specified URL and displays it in DIV#hello using jQuery.

$(document).ready(function() {
    // Define the URL to fetch the translation
    const apiUrl = "https://fourtonfish.com/hellosalut/?lang=fr";
  
    // Use the jQuery AJAX function to make a GET request to the URL
    $.ajax({
      url: apiUrl,
      type: "GET",
      success: function(data) {
        // Extract the translation from the response data
        const translation = data.hello;
  
        // Display the translation in the DIV#hello
        $('#hello').text(translation);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        // Handle errors, if any
        console.log(`Error: ${textStatus}`);
      }
    });
  });  