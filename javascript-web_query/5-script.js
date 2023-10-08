#!/usr/bin/node
// This JavaScript script adds a <li> element to UL.my_list when the user clicks on the tag DIV#add_item using jQuery.

$(document).ready(function() {
    // Use the jQuery API to select the <div> element with id "add_item"
    const addItem = $('#add_item');
  
    // Use the jQuery API to select the <ul> element with class "my_list"
    const myList = $('ul.my_list');
  
    // Define a click event handler for the "DIV#add_item"
    addItem.click(function() {
      // Create a new <li> element
      const newListItem = $('<li>Item</li>');
      
      // Append the new <li> element to the <ul.my_list>
      myList.append(newListItem);
    });
  });  