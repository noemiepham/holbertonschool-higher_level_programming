#!/usr/bin/node

const fs = require('fs');
const PathFile = process.argv[2];
const StringFile = process.argv[3];
fs.writeFile(PathFile, StringFile, 'utf-8', function (err, data) {
  if (err) throw err;
});
