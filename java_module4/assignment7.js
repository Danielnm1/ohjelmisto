'use strict';

const form = document.getElementById('addrForm');
const input = document.getElementById('addrInput');
const tripInfo = document.getElementById('tripInfo');

const map = L.map('map').setView([60.192, 24.945], 13);


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors',
}).addTo(map);

// School coordinates
const schoolCoords = L.latLng(60.21766, 24.93698); // Karaportti 2
L.marker(schoolCoords).addTo(map).bindPopup('Karaportti 2');

let control; // Route control variable

// Mock function for converting user address to coordinates
function mockGeocode(address) {
  const lat = schoolCoords.lat - 0.01 + Math.random() * 0.02;
  const lng = schoolCoords.lng - 0.01 + Math.random() * 0.02;
  return L.latLng(lat, lng);
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const addr = input.value.trim();
  if (!addr) return alert('Please enter an address!');


  if (control) map.removeControl(control);

  const userCoords = mockGeocode(addr);


  control = L.Routing.control({
    waypoints: [
      userCoords,
      schoolCoords,
    ],
    routeWhileDragging: false,
    showAlternatives: false,
    addWaypoints: false,
    lineOptions: {styles: [{color: 'blue', weight: 5}]},
    createMarker: (i, wp) => L.marker(wp.latLng),
  }).addTo(map);


  const startTime = new Date();
  const endTime = new Date(startTime.getTime() + 15 * 60 * 1000); // +15 minutes
  tripInfo.textContent = `Trip starts at ${startTime.toLocaleTimeString()}, ends at ${endTime.toLocaleTimeString()}`;
});
