#!/usr/bin/node

let argumentCount = 0;

exports.logMe = function (item) {
  console.log(`${argumentCount}: ${item}`);
  argumentCount++;
};
