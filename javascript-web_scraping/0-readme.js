#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // The file path is the first argument passed to the script

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred
  } else {
    console.log(data); // Print the content of the file
  }
});
