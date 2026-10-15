from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
COUNTDOWN = ROOT / "_assets/remote/embed/codelet/cec7jjfpy59ze5m1/index.html"
RSVP = ROOT / "_assets/widget.html"


class EmbeddedSectionTests(unittest.TestCase):
    def test_existing_countdown_embed_targets_wedding_datetime(self):
        content = COUNTDOWN.read_text(encoding="utf-8")
        self.assertIn("2027-01-09T14:00:00-06:00", content)
        self.assertIn("DÍAS", content)
        self.assertIn("HORAS", content)
        self.assertIn("MINUTOS", content)
        self.assertNotIn('class="title"', content)
        self.assertNotIn('class="caption"', content)

    def test_existing_rsvp_embed_is_a_contact_form(self):
        content = RSVP.read_text(encoding="utf-8")
        self.assertIn('id="rsvp-form"', content)
        self.assertIn('name="nombre"', content)
        self.assertIn('name="asistencia"', content)
        self.assertIn("¿Podrás acompañarnos en nuestro gran día?", content)
        self.assertIn("Sí, ahí estaré!", content)
        self.assertIn("No podré asistir, pero los llevo en mi corazón", content)
        self.assertIn("font-size:22px", content)
        self.assertIn("height:22px", content)
        self.assertIn("min-height:60px", content)
        self.assertIn('font:16px "Times New Roman",serif', content)
        self.assertIn("white-space:nowrap", content)
        self.assertNotIn('class="question"', content)
        self.assertIn("overflow:hidden", content)
        self.assertIn("transform:scale(1.2)", content)
        self.assertNotIn('class="notice"', content)


if __name__ == "__main__":
    unittest.main()
