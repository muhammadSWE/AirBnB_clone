#!/usr/bin/python3
'''
Unit tests module for the Amenity class
'''
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    '''
    Unit tests for the Amenity class
    '''

    def setUp(self) -> None:
        '''
        Set up for each test
        '''
        self.amenity = Amenity()

    def test_inheritance(self):
        '''
        Test that the Amenity class inherits from BaseModel
        '''
        self.assertIsInstance(self.amenity, BaseModel)

    def test_class(self):
        '''
        Test that the Amenity class is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def test_name_attr(self):
        '''
        Tests the existance, data type, and default value of the
        name attribute
        '''
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
