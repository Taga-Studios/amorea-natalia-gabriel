from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InvitationCloneTests(unittest.TestCase):
    def test_invitation_is_a_standalone_editable_site(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        config = (ROOT / "config.js").read_text(encoding="utf-8")
        app = (ROOT / "app.js").read_text(encoding="utf-8")

        self.assertIn('src="config.js"', index)
        self.assertIn('src="app.js"', index)
        self.assertIn("Natalia Garcia", config)
        self.assertIn("Gabriel Meza", config)
        self.assertNotIn("invite.amoreaestudio.com", index + app)
        self.assertNotIn("invite.amoreaestudio.com", config)

    def test_config_has_all_editable_client_details(self):
        config = (ROOT / "config.js").read_text(encoding="utf-8")
        keys = [
            "couple", "date", "ceremony", "reception", "cocktail", "venue",
            "address", "mapUrl", "rsvpDeadline", "dressCode", "giftMessage",
            "heroImage", "gallery", "musicUrl"
        ]
        for key in keys:
            self.assertRegex(config, rf"\b{key}\s*:", key)

    def test_countdown_is_implemented_without_a_framework_runtime(self):
        app = (ROOT / "app.js").read_text(encoding="utf-8")
        self.assertIn("setInterval", app)
        self.assertIn("countdown", app)
        self.assertIn("new Date", app)


if __name__ == "__main__":
    unittest.main()
