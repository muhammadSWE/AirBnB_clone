#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Unit tests for the State class """

    def test_inheritance(self):
        """ Test if State inherits from BaseModel """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """ Test the presence of the 'name' attribute """
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_default_values(self):
        """ Test if 'name' has an empty string default """
        state = State()
        self.assertEqual(state.name, "")

    def test_data_types(self):
        """ Test if the 'name' attribute is a string """
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == "__main__":
    unittest.main()
