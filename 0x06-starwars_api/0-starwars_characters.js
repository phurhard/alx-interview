#!/usr/bin/node
const request = require('request');
const movie = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movie}`,
  function (err, res, body) {
    body = JSON.parse(body);
	  const characters = body.characters
	  for (const character of characters) {
		  request(character, function(err, res, body) {
			  person = JSON.parse(body)
			  console.log(person.name)
		  })
	  }
  });
