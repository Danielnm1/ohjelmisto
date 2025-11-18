

const numDice = parseInt(prompt("Enter the number of dice:"), 10);


const targetSum = parseInt(prompt("Enter the desired sum:"), 10);


const simulations = 10000;

let successCount = 0;


for (let i = 0; i < simulations; i++) {
  let sum = 0;


  for (let d = 0; d < numDice; d++) {
    const roll = Math.floor(Math.random() * 6) + 1;  // 1–6
    sum += roll;
  }


  if (sum === targetSum) {
    successCount++;
  }
}


const probability = (successCount / simulations) * 100;


document.getElementById("output").textContent =
  `Probability to get sum ${targetSum} with ${numDice} dice is ${probability.toFixed(2)}%.`;
