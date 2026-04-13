from subprocess import run
import unittest

from chatwork_bot.responder import build_local_response


class ResponderTests(unittest.TestCase):
    def test_build_response_bug(self) -> None:
        text = build_local_response("There is a BUG in production")
        self.assertIn("reproduction steps", text.lower())

    def test_cli(self) -> None:
        result = run(
            ["python3", "cli.py", "--message", "deploy update"],
            check=True,
            text=True,
            capture_output=True,
        )
        self.assertIn("deployment checklist", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
