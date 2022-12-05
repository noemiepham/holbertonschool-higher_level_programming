#!/usr/bin/node

const args = process.argv;
let index = 0;
let MaxNumber = 0;
while (index in args) {
  if (args[index] >= MaxNumber) {
    MaxNumber = args[index - 1];
  }
  index++;
}
if (index === 2) {
  console.log(0);
} else if (index === 3) {
  console.log(0);
} else {
  console.log(MaxNumber);
}
