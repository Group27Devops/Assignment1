import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Food Recipe App', response.data)

    def test_dishes_page(self):
        response = self.app.get('/dishes')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Dishes', response.data)

    def test_recipe_page(self):
        response = self.app.get('/recipe/52772')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teriyaki Chicken Casserole', response.data)

if __name__ == '__main__':
    unittest.main()
