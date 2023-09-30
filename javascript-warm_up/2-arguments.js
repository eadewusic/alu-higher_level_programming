#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements of process.argv

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
