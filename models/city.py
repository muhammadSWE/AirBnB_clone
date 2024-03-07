#!/usr/bin/python3
'''
This module contains the code for the City class.
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Definition of the City class based on BaseModel.
    '''
    state_id = ""
    name = ""
