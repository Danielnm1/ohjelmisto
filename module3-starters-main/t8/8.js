'use strict';

// Select elements
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const operationSelect = document.getElementById('operation');
const resultPara = document.getElementById('result');
const button = document.getElementById('start');

// Add click event listener
button.addEventListener('click', function() {
  // Get values and convert to numbers
  const num1 = parseFloat(num1Input.value);
  const num2 = parseFloat(num2Input.value);
  const operation = operationSelect.value;

  // Check if inputs are valid numbers
  if (isNaN(num1) || isNaN(num2)) {
    resultPara.textContent = 'Please enter valid numbers';
    return;
  }

  let result;

  // Perform calculation based on selected operation
  switch (operation) {
    case 'add':
      result = num1 + num2;
      break;
    case 'sub':
      result = num1 - num2;
      break;
    case 'multi':
      result = num1 * num2;
      break;
    case 'div':
      if (num2 === 0) {
        resultPara.textContent = 'Division by zero is not allowed';
        return;
      }
      result = num1 / num2;
      break;
    default:
      resultPara.textContent = 'Unknown operation';
      return;
  }

  // Display result
  resultPara.textContent = `Result: ${result}`;
});
