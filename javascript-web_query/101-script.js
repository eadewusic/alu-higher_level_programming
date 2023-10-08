#!/usr/bin/node
// This JavaScript script adds, removes, and clears LI elements from a list using the jQuery API.

$(document).ready(function() {
    // Define the UL.my_list element
    const myList = $('.my_list');
  
    // When the user clicks on DIV#add_item
    $('#add_item').click(function() {
      // Add a new <li> element with the text "Item" to the list
      myList.append($('<li>').text('Item'));
    });
  
    // When the user clicks on DIV#remove_item
    $('#remove_item').click(function() {
      // Remove the last <li> element from the list
      myList.children('li:last').remove();
    });
  
    // When the user clicks on DIV#clear_list
    $('#clear_list').click(function() {
      // Remove all <li> elements from the list
      myList.empty();
    });
  });  