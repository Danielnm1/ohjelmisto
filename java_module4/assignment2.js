'use strict';

const form = document.getElementById('searchForm');
const input = document.getElementById('query');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Stop the page from reloading

  const searchValue = input.value.trim();
  if (!searchValue) {
    console.log('Please enter a TV show name');
    return;
  }

  const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(
      searchValue)}`;

  fetch(url).then(response => response.json()).then(data => {
    console.log('Search results:', data);
  }).catch(error => {
    console.error('Error fetching data:', error);
  });
});
