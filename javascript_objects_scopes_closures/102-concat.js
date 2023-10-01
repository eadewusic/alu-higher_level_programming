#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: 102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

try {
  const content1 = fs.readFileSync(sourceFile1, 'utf8');
  const content2 = fs.readFileSync(sourceFile2, 'utf8');
  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destinationFile, concatenatedContent);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
