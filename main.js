const tg = window.Telegram.WebApp;
tg.ready();  // Telegram SDK активен

// Инициализация карты
const map = L.map('map').setView([15.8800, 108.0800], 16);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Геолокация пользователя
navigator.geolocation.getCurrentPosition(
  (pos) => {
    const { latitude, longitude } = pos.coords;
    map.setView([latitude, longitude], 16);
    L.marker([latitude, longitude])
      .addTo(map)
      .bindPopup("Вы здесь")
      .openPopup();
  },
  (err) => console.warn("Геолокация недоступна", err)
);

// Загружаем заведения с сервера
fetch("http://localhost:5000/api/places")  // !!! В Vercel будет другая ссылка
  .then(res => res.json())
  .then(places => {
    places.forEach(place => {
      L.marker([place.lat, place.lng])
        .addTo(map)
        .bindPopup(`<b>${place.name}</b><br>Скидка: ${place.discount}`);
    });
  })
  .catch(err => console.error("Ошибка загрузки заведений:", err));