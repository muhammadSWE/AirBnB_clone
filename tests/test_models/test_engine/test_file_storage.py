#!/usr/bin/python3
'''
Unit tests for the FileStorage class
'''
import json
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Unit tests for the FileStorage class """

    def setUp(self):
        """ Set up for each test, potentially removing the file.json """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """ Clean up after each test """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """ Test the `all` method """
        storage = FileStorage()
        self.assertEqual(storage.all(), FileStorage.__objects)

    def test_new(self):
        """ Test the `new` method """
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())

    def test_save(self):
        """ Test the `save` method """
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json") as f:
            file_data = json.load(f)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, file_data)

    def test_reload(self):
        """ Test the `reload` method """
        storage = FileStorage()
        # Create a simple dictionary to save
        test_dict = {"BaseModel.12345":
                     {"id": "12345", "__class__": "BaseModel"}}
        with open("file.json", "w") as f:
            json.dump(test_dict, f)

        # Call reload
        storage.reload()
        self.assertIn("BaseModel.12345", storage.all())


if __name__ == "__main__":
    unittest.main()
