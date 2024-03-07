#!/usr/bin/python3
'''
This module contains the code for the User class.
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Definition of the User class based on BaseModel.
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
