#!/usr/bin/python3
"""
contains the student function
"""


class Student:
    """representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """retrieves a dictionary representation of a Student"""
            return self.__dict__
