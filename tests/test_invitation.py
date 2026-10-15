from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InvitationCloneTests(unittest.TestCase):
    def test_recovered_invitation_has_its_local_runtime_and_assets(self):
        index = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("window['bootstrap']", index)
        self.assertIn("_assets/40d967428c12c1c7.runtime.js", index)
        self.assertTrue((ROOT / "_assets" / "693295d000114bc3.js").is_file())


if __name__ == "__main__":
    unittest.main()
