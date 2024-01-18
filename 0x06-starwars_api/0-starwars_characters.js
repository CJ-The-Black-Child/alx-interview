#!/usr/bin/node
const request = require('request')

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const API_URL = `https://swapi.dev/api/films/${movieId}/`;

  request(API_URL, (err, _, body) => {
    if (err) {
      console.error(err)
    }
    const charactersURL = JSON.parse(body).characters
    const charactersName = charactersURL.map(url => new Promise((resolve, reject) => {
      request(url, (promiseErr, __, charactersReqBody) => {
        if (promiseErr) {
          reject(promiseErr)
        }
        resolve(JSON.parse(charactersReqBody).name)
      })
    }))

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr))
  })
}
