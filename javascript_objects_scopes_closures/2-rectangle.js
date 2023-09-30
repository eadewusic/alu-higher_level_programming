#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w === 'undefined' || typeof h === 'undefined') {
      // If either w or h is not a positive integer or is 0, or if either is undefined, create an empty object.
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
