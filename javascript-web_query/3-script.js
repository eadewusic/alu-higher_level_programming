#!/usr/bin/node
// This JavaScript script adds the class "red" to the <header> element when the user clicks on the tag DIV#red_header using jQuery.

$(document).ready(function() {
    // Use the jQuery API to select the <div> element with id "red_header"
    const redHeader = $('#red_header');
  
    // Define a click event handler
    redHeader.click(function() {
      // Add the "red" class to the <header> element
      $('header').addClass('red');
    });
  });
  