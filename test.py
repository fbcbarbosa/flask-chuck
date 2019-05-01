import unittest
from app import app


class TestApp(unittest.TestCase):
    def test_joke(self):
        app.testing = True

        val = app.test_client().get("/")
        self.assertIn("Chuck", str(val.data))


if __name__ == "__main__":
    unittest.main()
