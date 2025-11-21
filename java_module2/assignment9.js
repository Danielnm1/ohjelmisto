
function even(array) {
  let evens = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      evens.push(array[i]);
    }
  }
  return evens;
}


const numbers = [2, 7, 4, 9, 10];


const evenNumbers = even(numbers);


console.log("Original array:", numbers);
console.log("Even numbers array:", evenNumbers);

