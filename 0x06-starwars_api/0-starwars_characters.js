#!/usr/bin/node
const request = require('request');

function getCharacterName(url) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      const json = JSON.parse(body);
      console.log(json.name);
    }
  });
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    const json = JSON.parse(body);
    for (let i = 0; i < json.characters.length; i++) {
      getCharacterName(json.characters[i]);
    }
  }
});
