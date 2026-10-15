(() => {
  const data = window.INVITATION;
  const $ = (id) => document.getElementById(id);
  document.title = `${data.couple.first} & ${data.couple.second}`;
  $("names").innerHTML = `${data.couple.first}<em>&</em>${data.couple.second}`;
  $("date-label").textContent = data.dateLabel;
  $("hero-image").src = data.heroImage;
  $("city").textContent = data.city;
  $("ceremony").textContent = data.ceremony;
  $("reception").textContent = data.reception;
  $("cocktail").textContent = data.cocktail;
  $("venue").textContent = data.venue;
  $("address").textContent = data.address;
  $("map-link").href = data.mapUrl;
  $("dress-code").textContent = data.dressCode;
  $("gifts").textContent = data.giftMessage;
  $("deadline").textContent = data.rsvpDeadline;
  $("rsvp-link").href = data.rsvpUrl;
  $("gallery").replaceChildren(...data.gallery.map((src, i) => {
    const image = new Image(); image.src = src; image.alt = `Natalia y Gabriel ${i + 1}`; return image;
  }));
  const updateCountdown = () => {
    let diff = Math.max(0, new Date(data.date).getTime() - Date.now());
    const values = [86400000, 3600000, 60000, 1000].map((unit) => {
      const result = Math.floor(diff / unit); diff -= result * unit; return String(result).padStart(2, "0");
    });
    $("countdown").replaceChildren(...values.map((value) => Object.assign(document.createElement("b"), { textContent: value })));
  };
  updateCountdown();
  setInterval(updateCountdown, 1000);
})();
