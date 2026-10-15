(() => {
  const target = new Date("2027-01-09T14:00:00-06:00");
  const style = document.createElement("style");
  style.textContent = `
    #atlas-countdown{position:fixed;right:18px;bottom:18px;z-index:99999;background:#304254;color:#fff;border:1px solid #d8c7b1;border-radius:14px;padding:14px 16px;box-shadow:0 8px 30px #0006;text-align:center;font-family:Georgia,serif;min-width:238px}#atlas-countdown .label{font-size:15px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:7px}#atlas-countdown .time{display:flex;gap:9px;justify-content:center}#atlas-countdown b{display:block;font-size:25px;line-height:1}#atlas-countdown small{font:10px Arial,sans-serif;text-transform:uppercase;letter-spacing:.08em}.atlas-rsvp{max-width:560px;margin:48px auto;padding:34px 24px;background:#304254;color:#fff;text-align:center;font-family:Georgia,serif}.atlas-rsvp h2{font-weight:400;font-size:34px;margin:0 0 8px}.atlas-rsvp p{font:16px Arial,sans-serif}.atlas-rsvp form{display:grid;gap:12px;text-align:left}.atlas-rsvp input,.atlas-rsvp select,.atlas-rsvp textarea{width:100%;padding:12px;border:0;border-radius:3px;font:15px Arial,sans-serif}.atlas-rsvp button{padding:13px;background:#d8c7b1;border:0;color:#304254;text-transform:uppercase;letter-spacing:.1em;font-weight:700;cursor:pointer}.atlas-rsvp .thanks{display:none;margin-top:14px}@media(max-width:600px){#atlas-countdown{left:12px;right:12px;bottom:12px;min-width:0}.atlas-rsvp{margin:32px 14px}}
  `;
  document.head.append(style);
  const countdown = document.createElement("aside");
  countdown.id = "atlas-countdown";
  countdown.innerHTML = '<div class="label">Faltan</div><div class="time"><span><b data-unit="days">00</b><small>días</small></span><span><b data-unit="hours">00</b><small>horas</small></span><span><b data-unit="minutes">00</b><small>min</small></span><span><b data-unit="seconds">00</b><small>seg</small></span></div>';
  document.body.append(countdown);
  const update = () => {
    let seconds = Math.max(0, Math.floor((target - new Date()) / 1000));
    const values = { days: Math.floor(seconds / 86400) };
    seconds %= 86400; values.hours = Math.floor(seconds / 3600);
    seconds %= 3600; values.minutes = Math.floor(seconds / 60); values.seconds = seconds % 60;
    Object.entries(values).forEach(([key, value]) => countdown.querySelector(`[data-unit="${key}"]`).textContent = String(value).padStart(2, "0"));
  };
  update(); setInterval(update, 1000);
  const rsvp = document.createElement("section");
  rsvp.className = "atlas-rsvp";
  rsvp.innerHTML = `<h2>Confirmar asistencia</h2><p>Nos encantará celebrar contigo.</p><form id="rsvp-form"><input required name="nombre" placeholder="Nombre completo"><select required name="asistencia"><option value="">¿Podrás asistir?</option><option>Sí, asistiré</option><option>No podré asistir</option></select><input name="acompanantes" type="number" min="0" placeholder="Número de acompañantes"><textarea name="mensaje" rows="3" placeholder="Mensaje para los novios (opcional)"></textarea><button type="submit">Enviar confirmación</button></form><p class="thanks">¡Gracias! Tu confirmación quedó registrada en esta página.</p>`;
  document.body.append(rsvp);
  rsvp.querySelector("form").addEventListener("submit", event => { event.preventDefault(); event.currentTarget.style.display = "none"; rsvp.querySelector(".thanks").style.display = "block"; });
})();
