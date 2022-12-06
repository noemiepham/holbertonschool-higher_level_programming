#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    if (size && size >= 0) {
      this.width = size;
      this.height = size
    }
  }

  print () {
    for (let row = 0; row < this.width; row++) {
      for (let col = 0; col < this.height; col++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Square;
