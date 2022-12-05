#!/usr/bin/node

function add (a, b) {
  const rs = a + b;
  return rs;
}
const args = process.argv;
const rs = +args[2];
if (isNaN(rs)) {
  console.log(rs);
} else {
  console.log(add(+args[2], +args[3]));
}
