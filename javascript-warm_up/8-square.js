#!/usr/bin/node

const args = process.argv;
const rs = +args[2];
if (isNaN(rs)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < rs; row++) {
    for (let col = 0; col < rs; col++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
