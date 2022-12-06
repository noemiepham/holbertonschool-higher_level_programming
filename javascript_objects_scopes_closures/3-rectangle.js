#!/usr/bin/node

module.exports = class Rectangle {
  // Class methods
  constructor(w, h) {
    if (w < 0 || h < 0) {
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
}
