#!/usr/bin/node

process.argv.forEach((val, index) => {
  if (index === 1) {
    console.log('No argument');
  }
  console.log(`${val}`);
});
