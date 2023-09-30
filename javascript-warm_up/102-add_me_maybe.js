#!/usr/bin/node

function addMeMaybe(number, theFunction) {
  const updatedNumber = number + 1;
  theFunction(updatedNumber);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
