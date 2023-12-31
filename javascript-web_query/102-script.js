#!/usr/bin/node
// This JavaScript script fetches and prints the translation of "Hello" based on the language code using the JQuery API.

$(document).ready(function() {
  // Define the click event handler for INPUT#btn_translate
  $('#btn_translate').click(function() {
    // Get the language code from INPUT#language_code
    const languageCode = $('#language_code').val();

    // Define the URL to fetch the translation
    const apiUrl = `http://localhost:8080/https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    // Note: The `?lang=${languageCode}` part of the URL is where the language code you input is inserted into the URL to request the translation in the desired language to allow the API to provide translations in different languages

    // Use the jQuery AJAX function to make a GET request to the URL
    $.ajax({
      url: apiUrl,
      type: "GET",
      success: function(data) {
        // Extract the translation from the response data
        const translation = data.hello;

        // Display the translation in DIV#hello
        $('#hello').text(translation);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        // Handle errors, if any
        console.log(`Error: ${textStatus}`);
      }
    });
  });
});