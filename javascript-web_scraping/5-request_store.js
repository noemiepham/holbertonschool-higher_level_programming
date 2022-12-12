#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const FilePath = process.argv[3];
request(URL, function (error, response, data) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(FilePath, 'utf-8', function (err, data) {
      if (err) {
        console.log(error);
      }
    });
  }
});
