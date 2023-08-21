#!/usr/bin/python3

"""State Module file"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class
    Attributes:
        name (str): name of state

    Methods:
        __init__: Constructor of the State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State instance"""
        super().__init__(*args, **kwargs)
