from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InvitationCustomizationTests(unittest.TestCase):
    def test_custom_script_has_target_countdown_and_rsvp_form(self):
        script = (ROOT / "custom.js").read_text(encoding="utf-8")
        self.assertIn("2027-01-09T14:00:00-06:00", script)
        self.assertIn('id="rsvp-form"', script)
        self.assertIn('name="nombre"', script)
        self.assertIn('name="asistencia"', script)


if __name__ == "__main__":
    unittest.main()
