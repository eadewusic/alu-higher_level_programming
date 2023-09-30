#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function incr() {
    this.value++;
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
