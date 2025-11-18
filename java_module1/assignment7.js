
const rolls = parseInt(prompt("How many dice rolls?"), 10);

let sum = 0;


for (let i = 0; i < rolls; i++) {
  // Random number between 1 and 6
  const roll = Math.floor(Math.random() * 6) + 1;
  sum += roll;
}


document.getElementById("output").textContent =
  `The sum of ${rolls} dice rolls is ${sum}.`;
