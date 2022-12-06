#!/usr/bin/node

function findSecondLargestElem (arr) {
  let first = -1;
  let second = -1;

  for (let i = 0; i <= arr.length - 1; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }
  console.log(second);
}

const args = process.argv;
let index = 2;
const table = [];

while (index in args) {
  table.push(+args[index]);
  index++;
}

if (index === 2) {
  console.log(0);
} else if (index === 3) {
  console.log(0);
} else {
  findSecondLargestElem(table);
}
