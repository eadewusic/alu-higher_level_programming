#!/usr/bin/node
// This JavaScript script updates the text color of the <header> element to red using jQuery.

// Wait for the DOM to fully load before executing the script
$(document).ready(function() {
    // Use the jQuery API to select the <header> element
    const header = $('header');
  
    // Update the text color of the <header> element to red (#FF0000) using the .css() method
    header.css('color', '#FF0000');
  });  