#!/usr/bin/node
// This JavaScript script updates the text color of the <header> element to red when the user clicks on the tag DIV#red_header using jQuery.

$(document).ready(function() {
  // Use the jQuery API to select the <div> element with id "red_header"
  const redHeader = $('#red_header');

  // Define a click event handler
  redHeader.click(function() {
    // Update the text color of the <header> element to red (#FF0000) using the .css() method
    $('header').css('color', '#FF0000');
  });
});