#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(arg, 10);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
