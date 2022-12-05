#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const args = process.argv;
const rs = +args[2];
if (isNaN(rs)) {
  console.log(1);
} else {
  console.log(factorial(rs));
}
