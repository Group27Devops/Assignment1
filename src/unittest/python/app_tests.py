#!/usr/bin/python
from unittest import TestCase
from app import app

class AppTest(TestCase):

    def test_hello_world(self):
        response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello, World!")
