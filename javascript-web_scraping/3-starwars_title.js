#!/usr/bin/node

const request = require('request');
const IdFilm = process.argv[2];
const PathUrl = `https://swapi-api.hbtn.io/api/films/${IdFilm}`;
request.get(PathUrl, function (error, response, data) {
  if (error) {
    return console.log(error);
  } else {
    console.log(JSON.parse(data).title);
  }
});
