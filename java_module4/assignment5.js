'use strict';

const url = 'https://api.chucknorris.io/jokes/random';

fetch(url).then(response => response.json()).then(data => {
  console.log('Chuck Norris Joke:', data.value);
}).catch(error => {
  console.error('Error fetching joke:', error);
});
