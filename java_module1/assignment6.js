
const shouldCalculate = confirm("Should I calculate the square root?");
let result;

if (shouldCalculate) {

  const number = parseFloat(prompt("Enter a number:"));

  if (number < 0) {
    result = "The square root of a negative number is not defined.";
  } else {
    const sqrt = Math.sqrt(number);
    result = `The square root of ${number} is ${sqrt}.`;
  }

} else {

  result = "The square root is not calculated.";
}

document.getElementById("output").textContent = result;
