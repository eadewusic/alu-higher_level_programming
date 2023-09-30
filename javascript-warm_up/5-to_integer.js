#!/usr/bin/node

const arg1 = process.argv[2];

if (!isNaN(arg1) && Number.isInteger(parseInt(arg1, 10))) {
  console.log(`My number: ${parseInt(arg1, 10)}`);
} else {
  console.log('Not a number');
}
