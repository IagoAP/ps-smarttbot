import unittest
import json

from app import app

class TestHome(unittest.TestCase):

    def test_post(self):
        server = app.test_client()
        response = server.post('/')
        rows = json.loads(response.get_data(as_text=True))
        row = rows[0]
        self.assertEqual(200, response.status_code)
        self.assertEqual(row['moeda'], "Bitcoin")
        self.assertEqual(row['periodicidade'], int("1"))
        self.assertEqual(row['open'], int("2"))
        self.assertEqual(row['low'], int("1"))
        self.assertEqual(row['high'], int("4"))
        self.assertEqual(row['close'], int("3"))
        row = rows[1]
        self.assertEqual(200, response.status_code)
        self.assertEqual(row['moeda'], "Monero")
        self.assertEqual(row['periodicidade'], int("5"))
        self.assertEqual(row['open'], int("3"))
        self.assertEqual(row['low'], int("4"))
        self.assertEqual(row['high'], int("1"))
        self.assertEqual(row['close'], int("2"))

if __name__ == '__main__':
    unittest.main()