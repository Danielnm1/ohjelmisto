'use strict';

// Select the elements
const trigger = document.getElementById('trigger');
const target = document.getElementById('target');

// When mouse is over the <p>, change the image
trigger.addEventListener('mouseover', function() {
  target.src = 'img/picB.jpg';
});

// When mouse leaves the <p>, change the image back
trigger.addEventListener('mouseout', function() {
  target.src = 'img/picA.jpg';
});
