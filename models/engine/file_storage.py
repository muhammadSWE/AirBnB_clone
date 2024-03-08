#!/usr/bin/python3
'''
This module contains the code for the FileStorage class.

Classes:
    FileStorage: the file storage class
'''
import json
import datetime
import os
from models.base_model import BaseModel


class FileStorage:
    '''
    This class serializes instances to a JSON file and
    deserializes JSON file to instances.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns __objects dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets new obj in __objects dictionary
        '''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serialzes __objects to JSON file
        '''
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        '''
        Returns a dictionary of valid classes and their references
        '''
        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        '''
        Deserializes JSON file into __objects
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        '''
        Returns the valid attributes and their types for classname
        '''
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime}
                      }
        return attributes