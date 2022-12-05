#!/usr/bin/node

const args = process.argv;
const rs = +args[2];
if (isNaN(rs)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${rs}`);
}
