const tg = window.Telegram.WebApp;
tg.ready();  // Telegram SDK инициализирован

// Заведения со скидками (пока захардкожены)
const places = [
  { name: "Cup Coffee", lat: 15.8801, lng: 108.0812, discount: "25%" },
  { name: "Pho 79", lat: 15.8785, lng: 108.0827, discount: "15%" },
  { name: "Bamboo Spa", lat: 15.8770, lng: 108.0805, discount: "10%" }
];

// Инициализация карты
const map = L.map('map').setView([15.8800, 108.0800], 16);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Геолокация
navigator.geolocation.getCurrentPosition(
  (pos) => {
    const { latitude, longitude } = pos.coords;
    map.setView([latitude, longitude], 16);
    L.marker([latitude, longitude]).addTo(map).bindPopup("Вы здесь").openPopup();
  },
  (err) => console.warn("Не удалось получить геопозицию", err)
);

// Метки со скидками
places.forEach(place => {
  L.marker([place.lat, place.lng])
    .addTo(map)
    .bindPopup(`<b>${place.name}</b><br>Скидка: ${place.discount}`);
});