#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
	if (!error) {
		const results = JSON.parse(body).results;
		console.log(results.reduce((count, movie) => {
			if (movie.characters.find((character) => character.endsWith('/18/')))
				return count + 1;
			else
				return count;
		}, 0));
	}
});
