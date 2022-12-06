#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    if (size >= 0) {
      this.size = size;
    }
  }

  charPrint (c) {
    for (let row = 0; row < this.size; row++) {
      for (let col = 0; col < this.size; col++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      console.log();
    }
  }

  double () {
    this.size = this.size * 2;
  }
}

module.exports = Square;
