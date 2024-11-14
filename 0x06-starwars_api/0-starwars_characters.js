#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charURL = JSON.parse(body).characters;
    const charName = charURL.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (pErr, _, charReqBody) => {
          if (pErr) {
            reject(pErr);
          }
          resolve(JSON.parse(charReqBody).name);
        });
      });
    });

    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(aErr => console.log(aErr));
  });
}
