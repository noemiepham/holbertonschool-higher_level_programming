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
          for (let row = 0; row < this.height * 2; row++) {
               for (let col = 0; col < this.width * 2; col++) {
                 process.stdout.write('X');
               }
               console.log();
             }
     }
     rotate () {
          this.height = this.width;
          this.width = this.height;
          this.print = print()
     }
   }
   module.exports = Rectangle;