#!/usr/bin/node
// This JavaScript script fetches and prints the translation of "Hello" based on the language code using the JQuery API.

$(document).ready(function() {
    // Define the API URL for the translation service
    const apiURL = 'https://www.fourtonfish.com/hellosalut/hello/';
    
    // Update the endpoint to use the local Express server's proxy route
    const endpoint = 'http://localhost:8080/proxy?lang=';
  
    // Define a function to fetch and display the translation
    function fetchTranslation() {
      // Get the language code from INPUT#language_code
      const lang = $('#language_code').val();
  
      // Make a GET request to the API URL with the selected language code
      $.get(apiURL + lang.toString(), function (data) {
        // Update DIV#hello with the fetched translation
        $('#hello').text(data.hello);
      });
    }
  
    // Trigger fetchTranslation when user clicks on INPUT#btn_translate
    $('#btn_translate').click(fetchTranslation);
  
    // Trigger fetchTranslation when Enter key is pressed while focused on INPUT#language_code
    $('#language_code').keypress(function(event) {
      if (event.keyCode === 13) {
        fetchTranslation();
      }
    });
  });  