'use strict';

const input = document.getElementById('calculation');
const button = document.getElementById('start');
const resultPara = document.getElementById('result');

button.addEventListener('click', function() {
  const calc = input.value.trim();

  let operator;
  if (calc.includes('+')) operator = '+';
  else if (calc.includes('-')) operator = '-';
  else if (calc.includes('*')) operator = '*';
  else if (calc.includes('/')) operator = '/';
  else {
    resultPara.textContent = 'Invalid calculation';
    return;
  }


  const parts = calc.split(operator);

  if (parts.length !== 2) {
    resultPara.textContent = 'Invalid calculation';
    return;
  }


  const num1 = parseInt(parts[0], 10);
  const num2 = parseInt(parts[1], 10);

  if (isNaN(num1) || isNaN(num2)) {
    resultPara.textContent = 'Invalid numbers';
    return;
  }

  let result;

  // Perform calculation
  switch (operator) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      if (num2 === 0) {
        resultPara.textContent = 'Division by zero is not allowed';
        return;
      }
      result = Math.floor(num1 / num2); // integer division
      break;
  }

  resultPara.textContent = `Result: ${result}`;
});
