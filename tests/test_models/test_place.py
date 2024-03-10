#!/usr/bin/python3
'''
Unit tests module for the Place class
'''
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    '''
    Unit tests for the Place class
    '''

    def setUp(self) -> None:
        '''
        Set up for each test
        '''
        self.place = Place()

    def test_inheritance(self):
        '''
        Test that the Place class inherits from BaseModel
        '''
        self.assertIsInstance(self.place, BaseModel)

    def test_class(self):
        '''
        Test that the Place class is a subclass of BaseModel
        '''
        self.assertTrue(issubclass(self.place.__class__, BaseModel))

    def test_name_attr(self):
        '''
        Tests the existance, data type, and default value of the
        name attribute
        '''
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")
        self.assertIsInstance(self.place.name, str)

    def test_city_id_attr(self):
        '''
        Tests the existance, data type, and default value of the
        city_id attribute
        '''
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_attr(self):
        '''
        Tests the existance, data type, and default value of the
        user_id attribute
        '''
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertIsInstance(self.place.user_id, str)

    def test_description_attr(self):
        '''
        Tests the existance, data type, and default value of the
        description attribute
        '''
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_attr(self):
        '''
        Tests the existance, data type, and default value of the
        number_rooms attribute
        '''
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_attr(self):
        '''
        Tests the existance, data type, and default value of the
        number_bathrooms attribute
        '''
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_attr(self):
        '''
        Tests the existance, data type, and default value of the
        max_guest attribute
        '''
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_attr(self):
        '''
        Tests the existance, data type, and default value of the
        price_by_night attribute
        '''
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_attr(self):
        '''
        Tests the existance, data type, and default value of the
        latitude attribute
        '''
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_attr(self):
        '''
        Tests the existance, data type, and default value of the
        longitude attribute
        '''
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_attr(self):
        '''
        Tests the existance, data type, and default value of the
        amenity_ids attribute
        '''
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
