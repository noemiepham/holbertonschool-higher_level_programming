#!/usr/bin/node

const request = require('request');
const PathUrl = process.argv[2];
request.get(PathUrl, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log(`Code: ${response.statusCode}`);
  }
});
