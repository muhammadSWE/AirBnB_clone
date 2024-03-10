#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Unit tests for the City class """

    def test_inheritance(self):
        """ Test if City inherits from BaseModel """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """ Test the presence of 'state_id' and 'name' attributes """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_default_values(self):
        """ Test if 'state_id' and 'name' have empty string defaults """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_data_types(self):
        """ Test if 'state_id' and 'name' attributes are strings """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == "__main__":
    unittest.main()
