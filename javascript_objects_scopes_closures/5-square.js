#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    if (size >= 0) {
      this.size = size;
    }
  }

  print () {
    for (let row = 0; row < this.size; row++) {
      for (let col = 0; col < this.size; col++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  double () {
    this.size = this.size * 2;
  }
}
module.exports = Square;
