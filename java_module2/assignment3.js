

let dogs = [];


for (let i = 0; i < 6; i++) {
  const name = prompt(`Enter name of dog ${i + 1}:`);
  dogs.push(name);
}


dogs.sort();      // normal alphabetical order
dogs.reverse();   // reverse it


const list = document.getElementById("dog-list");

for (let i = 0; i < dogs.length; i++) {
  const li = document.createElement("li");
  li.textContent = dogs[i];
  list.appendChild(li);
}
