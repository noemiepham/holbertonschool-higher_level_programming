#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h && w >= 0 && h >= 0) {
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
    const a = this.height;
    const b = this.width;
    this.width = a;
    this.height = b;
  }
}

module.exports = Rectangle;
