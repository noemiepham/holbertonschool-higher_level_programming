#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request.get(URL, function (error, response, data) {
  if (error) {
    return console.log(error);
  } else {
     let count = 0;
     for (let i in JSON.parse(data).results){
          
     }
  }
});