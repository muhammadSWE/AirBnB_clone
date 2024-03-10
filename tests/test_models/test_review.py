#!/usr/bin/python3
'''
Unit tests module for the Review class
'''
import sys
sys.path.append('/home/danielkamel/AirBnB_clone')

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    '''
    Unit tests for the Review class
    '''

    def setUp(self) -> None:
        '''
        Set up for each test
        '''
        self.review = Review()

    def test_inheritance(self):
        '''
        Test that the Review class inherits from BaseModel
        '''
        self.assertIsInstance(self.review, BaseModel)

    def test_class(self):
        '''
        Test that the Review class is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def test_place_id_attr(self):
        '''
        Tests the existance, data type, and default value of the
        place_id attribute
        '''
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_attr(self):
        '''
        Tests the existance, data type, and default value of the
        user_id attribute
        '''
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertIsInstance(self.review.user_id, str)

    def test_text_attr(self):
        '''
        Tests the existance, data type, and default value of the
        text attribute
        '''
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")
        self.assertIsInstance(self.review.text, str)

if __name__ == "__main__":
    unittest.main()
