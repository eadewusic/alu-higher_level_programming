#!/usr/bin/node
// This JavaScript script fetches and prints the translation of "Hello" based on the language code using the JQuery API.
$(document).ready(function() {
    // Define the API endpoint
    const endpoint = 'https://www.fourtonfish.com/hellosalut/hello/';
  
    // Define a function to fetch and display the translation
    function fetchTranslation() {
      // Get the language code from INPUT#language_code
      const lang = $('#language_code').val();
  
      // Make a GET request to the API endpoint with the selected language code
      $.get(endpoint + lang.toString(), function (data) {
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