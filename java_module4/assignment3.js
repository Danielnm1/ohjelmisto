'use strict';

const form = document.getElementById('searchForm');
const input = document.getElementById('query');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Stop form from submitting

  const searchValue = input.value.trim();
  if (!searchValue) {
    alert('Please enter a TV show name');
    return;
  }

  const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(
      searchValue)}`;

  fetch(url).then(response => response.json()).then(data => {
    // Clear old results
    resultsDiv.innerHTML = '';

    // Loop through each show in the search results
    data.forEach(tvShow => {
      const show = tvShow.show;

      const article = document.createElement('article');

      // Name
      const h2 = document.createElement('h2');
      h2.textContent = show.name;

      const link = document.createElement('a');
      link.href = show.url;
      link.target = '_blank';
      link.textContent = 'More details';

      // Image (optional chaining to avoid errors)
      const img = document.createElement('img');
      img.src = show.image?.medium || '';
      img.alt = show.name;

      // Summary
      const summaryDiv = document.createElement('div');
      summaryDiv.innerHTML = show.summary || '';

      // Append all elements to article
      article.append(h2, link, img, summaryDiv);

      resultsDiv.appendChild(article);
    });
  }).catch(error => {
    console.error('Error fetching data:', error);
  });
});
