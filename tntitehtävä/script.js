const button = document.getElementById('fetchButton');
const container = document.getElementById('helloContainer');

button.addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/hello');
        const data = await response.json();

        console.log(data); // Tarkistetaan konsolista, että lista tulee oikein

        // Tyhjennä container ennen uuden listan lisäämistä
        container.innerHTML = '';

        // Käydään kaikki itemit läpi ja lisätään ne sivulle
        data.forEach(item => {
            const p = document.createElement('p');
            p.textContent = item;
            container.appendChild(p);
        });
    } catch (error) {
        console.error('Virhe haettaessa dataa:', error);
    }
});

