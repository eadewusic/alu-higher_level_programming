#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = parseInt(arg, 10);
  if (size < 1) {
    // Size is less than 1; no square to print.
  } else {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  }
}
