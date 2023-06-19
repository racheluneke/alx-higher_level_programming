#!/usr/bin/python3
"""my base moldel"""


class Base:
    """my base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is none:
            self.id =id
        else:
            self.id = __nb_objects + 1
            Base.__nb_objects + = 1
