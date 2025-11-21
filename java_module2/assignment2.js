
const count = Number(prompt("How many participants?"));

let participants = [];


for (let i = 0; i < count; i++) {
  const name = prompt(`Enter the name of participant ${i + 1}:`);
  participants.push(name);
}


participants.sort();


const list = document.getElementById("participant-list");

for (let i = 0; i < participants.length; i++) {
  const li = document.createElement("li");
  li.textContent = participants[i];
  list.appendChild(li);
}
