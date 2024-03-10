#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
import datetime


class TestBaseModel(unittest.TestCase):
    """ Unit tests for the BaseModel class """

    def test_init(self):
        # Test normal instantiation
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

        # Test instantiation with kwargs
        my_model2 = BaseModel(name="MyModel", age=89)
        self.assertEqual(my_model2.name, "MyModel")
        self.assertEqual(my_model2.age, 89)

    def test_str(self):
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"],
                         model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
