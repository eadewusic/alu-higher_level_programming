#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  n = parseInt(n, 10);

  if (n < 0) {
    return Infinity;
  }

  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const result = factorial(arg);
console.log(result);
