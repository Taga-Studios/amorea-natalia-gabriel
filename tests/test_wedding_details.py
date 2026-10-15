from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WeddingDetailsTests(unittest.TestCase):
    def test_invitation_contains_corrected_wedding_details(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        for expected in [
            "Odarlis Pérez", "Jose Tannous", "Kissimmee, Florida", "09 de Enero 2027",
            "Holy Cross Catholic Church", "2:00pm", "12600 Marsfield Ave, Orlando, FL 32837",
            "Studio 1060 Event Venue", "3:30pm",
            "Dc5ZC3PxHT1qYD7H6", "CBvFfmi8xAq17Y2P6",
            "2:00pm - Ceremonia • Holy Cross Catholic Church",
            "3:30pm - Recepción • Studio 1060 Event Venue",
        ]:
            self.assertIn(expected, page)
        for removed in ["Natalia Garcia", "Gabriel Meza", "Ciudad de Mexico, Mexico", "31 de Marzo 2026", "16:30 - Coctel"]:
            self.assertNotIn(removed, page)

    def test_envelope_photo_uses_the_couple_photo(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("_assets/media/odarlis-jose.jpg", page)
        self.assertTrue((ROOT / "_assets" / "media" / "odarlis-jose.jpg").is_file())
        self.assertIn('"A":-80.43545751633985,"B":65.0,"D":385.0', page)


if __name__ == "__main__":
    unittest.main()
