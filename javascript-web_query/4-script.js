#!/usr/bin/node
// This JavaScript script toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header using jQuery.

$(document).ready(function() {
    // Use the jQuery API to select the <div> element with id "toggle_header"
    const toggleHeader = $('#toggle_header');
    // Use the jQuery API to select the <header> element
    const header = $('header');
  
    // Define a click event handler for the "DIV#toggle_header"
    toggleHeader.click(function() {
      // Toggle the classes "red" and "green" on the <header> element
      header.toggleClass('red green');
    });
  });  