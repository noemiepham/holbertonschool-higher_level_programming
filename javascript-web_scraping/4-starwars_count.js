#!/usr/bin/node

const request = require('request');
const PathUrl = process.argv[2];
// const PathUrl = `https://swapi-api.hbtn.io/api/films/films/}`;
let counts = 0;
request(PathUrl, function (error, request, data) {
  if (error) {
    console.log(error);
  } else {
    for (const movie of JSON.parse(data).results) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          counts++;
        }
      }
    }
    console.log(counts);
  }
});
