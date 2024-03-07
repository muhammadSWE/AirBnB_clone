#!/usr/bin/python3
'''
This module contains the code for the Review class.
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Definition of the Review class based on BaseModel.
    '''
    place_id = ""
    user_id = ""
    text = ""
