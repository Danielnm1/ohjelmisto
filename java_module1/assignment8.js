// assignment8.js


const startYear = parseInt(prompt("Enter the start year:"), 10);
const endYear = parseInt(prompt("Enter the end year:"), 10);


function isLeapYear(year) {
  return (
    (year % 4 === 0 && year % 100 !== 0) ||
    (year % 400 === 0)
  );
}

let html = "<ul>";

for (let year = startYear; year <= endYear; year++) {
  if (isLeapYear(year)) {
    html += `<li>${year}</li>`;
  }
}

html += "</ul>";


document.getElementById("output").innerHTML = html;
