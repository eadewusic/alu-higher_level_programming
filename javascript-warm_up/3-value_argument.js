#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements of process.argv

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
