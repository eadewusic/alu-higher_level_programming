#!/usr/bin/node
// This JavaScript script updates the text of the <header> element to "New Header!!!" when the user clicks on DIV#update_header using jQuery.

$(document).ready(function() {
    // Use the jQuery API to select the <div> element with id "update_header"
    const updateHeader = $('#update_header');
  
    // Use the jQuery API to select the <header> element
    const header = $('header');
  
    // Define a click event handler for the "DIV#update_header"
    updateHeader.click(function() {
      // Update the text of the <header> element to "New Header!!!"
      header.text('New Header!!!');
    });
  });  