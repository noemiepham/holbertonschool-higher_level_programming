#!/usr/bin/node

const args = process.argv;
const rs = +args[2];
if (isNaN(rs)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < rs; i++) {
    console.log('C is fun');
  }
}
