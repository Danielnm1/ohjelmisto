

let numbers = [];
let duplicateFound = false;

while (!duplicateFound) {
  const num = Number(prompt("Enter a number:"));

  if (numbers.includes(num)) {
    console.log(`The number ${num} has already been entered. Stopping.`);
    duplicateFound = true;
  } else {
    numbers.push(num);
  }
}


numbers.sort(function(a, b) {
  return a - b;
});


console.log("All numbers entered (ascending order):");
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
