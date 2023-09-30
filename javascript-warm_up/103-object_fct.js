#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: () => {
    this.value++; // Use arrow function to maintain 'this' context
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
