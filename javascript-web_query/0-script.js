#!/usr/bin/node
// This JavaScript script updates the text color of the <header> element to red.

// Wait for the DOM to fully load before executing the script
document.addEventListener('DOMContentLoaded', function () {
  // Select the <header> element using document.querySelector
  const header = document.querySelector('header');
  
  // Update the text color of the <header> element to red (#FF0000)
  header.style.color = '#FF0000';
});
