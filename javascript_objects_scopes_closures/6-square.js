#!/usr/bin/node
const Square = require('./5-square');

class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }
}

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

module.exports = Rectangle;
module.exports = Square;
