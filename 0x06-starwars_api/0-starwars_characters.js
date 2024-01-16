#!/usr/bin/node
const request = require('request');
const movie = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie}`;
/**
 * While this code works fine, it does not take into consideration the format at which the names are placed on the endpoint
 * That's becomes the information are not really returned as it is been called, 
 * it needs to be called with await and async
 * 
request(`https://swapi-api.alx-tools.com/api/films/${movie}`,
  function (err, res, body) {
    console.log(err);
    body = JSON.parse(body);
    const characters = body.characters;
    console.log(characters)
    for (const character of characters) {
      console.log(character)
      request(character, function (error, res, body) {
        if (error) {return error;}
        const person = JSON.parse(body);
//        console.log(person.name);
      });
    }
  });
**/

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchData () {
  try {
    const data = await makeRequest(url);
    const dataJson = JSON.parse(data);
    const characters = dataJson.characters;
    for (const character of characters) {
      const Data = await makeRequest(character);
      const people = JSON.parse(Data);
      console.log(people.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
