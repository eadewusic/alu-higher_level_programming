#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function() {
    this.value++; // Use a regular function declaration
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
