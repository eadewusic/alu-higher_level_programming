#!/usr/bin/node

// Define the function
function add (a, b) {
  return a + b;
}

// Export the function so it can be used from outside
module.exports = {
  add
};
