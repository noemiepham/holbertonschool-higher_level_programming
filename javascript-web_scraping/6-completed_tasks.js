#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const newDic = {};
request(URL, function (error, response, data) {
  if (error) {
    console.log(error);
  } else {
    for (const task of JSON.parse(data)) {
      if (task.completed === true) {
        if (newDic[task.userId] === undefined) {
          newDic[task.userId] = 1;
        } else {
          newDic[task.userId] += 1;
        }
      }
    }
    console.log(newDic);
  }
});
