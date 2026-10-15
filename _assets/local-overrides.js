/*
 * Stable overrides for Canva's generated rich-text DOM.
 * Canva splits each visual line into spans; these rules force the two
 * ceremony-card lines to keep one white foreground color.
 */
(() => {
  const ceremonyLines = [
    'Holy Cross Catholic Church',
    '12600 Marsfield Ave, Orlando, FL 32837',
  ];

  const normalize = (value) => value.replace(/\s+/g, ' ').trim();

  function forceCeremonyTextWhite() {
    for (const paragraph of document.querySelectorAll('p')) {
      const text = normalize(paragraph.textContent || '');
      if (!ceremonyLines.some((line) => text === line)) continue;

      paragraph.style.setProperty('color', '#ffffff', 'important');
      for (const fragment of paragraph.querySelectorAll('*')) {
        fragment.style.setProperty('color', '#ffffff', 'important');
      }
    }
  }

  const observer = new MutationObserver(forceCeremonyTextWhite);
  observer.observe(document.documentElement, { childList: true, subtree: true });
  forceCeremonyTextWhite();
  window.addEventListener('load', forceCeremonyTextWhite, { once: true });
})();
