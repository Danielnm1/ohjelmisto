

const number = parseInt(prompt("Enter an integer:"), 10);

let message = "";


if (number <= 1) {
  message = `${number} is not a prime number.`;
} else {
  let isPrime = true;


  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      isPrime = false;
      break;
    }
  }

  if (isPrime) {
    message = `${number} is a prime number.`;
  } else {
    message = `${number} is NOT a prime number.`;
  }
}


document.getElementById("output").textContent = message;
