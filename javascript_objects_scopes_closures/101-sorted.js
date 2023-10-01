#!/usr/bin/node

const dict = require('./101-data').dict;

// Create a new dictionary to store user ids by occurrence
const userByOccurrence = {};

// Iterate through the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId];

  // Check if the occurrence exists in the new dictionary
  if (userByOccurrence[occurrence] === undefined) {
    userByOccurrence[occurrence] = [];
  }

  // Add the user id to the corresponding occurrence key
  userByOccurrence[occurrence].push(userId);
}

console.log(userByOccurrence);
