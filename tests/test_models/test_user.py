#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """ Unit tests for the User class """

    def test_inheritance(self):
        """ Test if User inherits from BaseModel """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """ Test the presence of expected attributes """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_default_values(self):
        """ Test for empty string defaults """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_data_types(self):
        """ Test if attributes are initialized as strings """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

if __name__ == "__main__":
    unittest.main()
