# Invitación editable — Natalia & Gabriel

Clon independiente y estático de la invitación pública autorizada. No requiere Canva ni conserva el runtime original.

## Editar

Modifica `config.js`:

- Nombres, fecha, textos, lugar, mapa, confirmación y dress code.
- `musicUrl`: pega una URL directa a un MP3 si quieres añadir música.
- `heroImage` y `gallery`: reemplaza las fotos locales dentro de `assets/`.

## Vista local

```bash
python3 -m http.server 4173
```

Abre `http://127.0.0.1:4173`.

## Publicación

Es un sitio estático: puede alojarse en Netlify, Vercel, GitHub Pages, Cloudflare Pages o cualquier hosting que sirva HTML/CSS/JS.

## Verificación

```bash
python3 -m unittest discover -s tests -v
node --check app.js && node --check config.js
```
