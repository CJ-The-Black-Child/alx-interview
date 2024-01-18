#!/usr/bin/node
const request = require('request')

function fetchCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) {
        reject(err)
      }
      resolve(JSON.parse(body).name)
    })
  })
}

async function fetchAndPrintCharacterNames(characterUrls) {
  for (const url of characterUrls) {
    const name = await fetchCharacterName(url)
    console.log(name)
  }
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const API_URL = `https://swapi.dev/api/films/${movieId}/`;

  request(API_URL, (err, _, body) => {
    if (err) {
      console.error(err)
    }
    const charactersURL = JSON.parse(body).characters
    fetchAndPrintCharacterNames(charactersURL)
    .catch(err => console.error(err))
  })
  }
