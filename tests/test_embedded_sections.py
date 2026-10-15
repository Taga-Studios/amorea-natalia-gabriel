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
        self.assertIn("SEGUNDOS", content)

    def test_existing_rsvp_embed_is_a_contact_form(self):
        content = RSVP.read_text(encoding="utf-8")
        self.assertIn('id="rsvp-form"', content)
        self.assertIn('name="nombre"', content)
        self.assertIn('name="asistencia"', content)


if __name__ == "__main__":
    unittest.main()
