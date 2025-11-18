
const year = parseInt(prompt("Enter a year:"), 10);

let message = "";


if (year % 400 === 0) {
  message = `${year} is a leap year.`;
} else if (year % 100 === 0) {
  message = `${year} is NOT a leap year.`;
} else if (year % 4 === 0) {
  message = `${year} is a leap year.`;
} else {
  message = `${year} is NOT a leap year.`;
}


document.getElementById("output").textContent = message;
