#!/usr/bin/node
// This JavaScript script updates the text color of the <header> element to red using document.querySelector.

document.addEventListener("DOMContentLoaded", function () {
    // Use document.querySelector to select the <header> element
    const header = document.querySelector("header");
  
    // Update the text color to red (#FF0000)
    header.style.color = "#FF0000";
  });  