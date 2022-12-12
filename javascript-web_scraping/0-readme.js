#!/usr/bin/node

const fs = require('fs');
const PathFile = process.argv[2];
fs.readFile(PathFile, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  } else {
    console.log(data.toString());
  }
});
