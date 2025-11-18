
const n1 = parseInt(prompt("Enter the first integer:"), 10);
const n2 = parseInt(prompt("Enter the second integer:"), 10);
const n3 = parseInt(prompt("Enter the third integer:"), 10);


const sum = n1 + n2 + n3;
const product = n1 * n2 * n3;
const average = sum / 3;


document.getElementById("output").innerHTML = `
  <p>Sum: ${sum}</p>
  <p>Product: ${product}</p>
  <p>Average: ${average}</p>
`;
