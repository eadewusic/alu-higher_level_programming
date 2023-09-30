#!/usr/bin/node

const args = process.argv.slice(2); // Remove the first two elements (script name and Node.js executable)

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // Sort the arguments in descending order
  console.log(args[1]);
}
