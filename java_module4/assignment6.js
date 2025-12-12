'use strict';

const form = document.getElementById('searchForm');
const input = document.getElementById('query');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const searchValue = input.value.trim();
  if (!searchValue) {
    alert('Please enter a search term');
    return;
  }

  const url = `https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(
      searchValue)}`;

  fetch(url).then(response => response.json()).then(data => {
    resultsDiv.innerHTML = '';
    if (data.total === 0) {
      resultsDiv.textContent = 'No jokes found.';
      return;
    }

    // Loop through each joke
    data.result.forEach(jokeObj => {
      const article = document.createElement('article');

      const p = document.createElement('p');
      p.textContent = jokeObj.value;

      article.appendChild(p);
      resultsDiv.appendChild(article);
    });
  }).catch(error => {
    console.error('Error fetching jokes:', error);
  });
});
