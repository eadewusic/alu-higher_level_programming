#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];  // The file path is the first argument passed to the script
const content = process.argv[3];   // The string to write is the second argument
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);  // Print the error object if an error occurred while writing
  }
});
