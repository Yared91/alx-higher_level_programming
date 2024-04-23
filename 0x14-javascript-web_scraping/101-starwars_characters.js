#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const content = JSON.parse(body);
        const characters = content.characters;

        const characterPromises = characters.map(character => {
            return new Promise((resolve, reject) => {
                request.get(character, (error, response, body) => {
                    if (error) {
                        reject(error);
                    } else {
                        const names = JSON.parse(body);
                        resolve(names.name);
                    }
                });
            });
        });

        Promise.all(characterPromises)
            .then(names => {
                names.forEach(name => {
                    console.log(name);
                });
            })
            .catch(error => {
                console.log(error);
            });
    }
});
