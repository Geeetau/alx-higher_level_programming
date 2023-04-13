#!usr/bin/python3
"""
contains the student function
"""


class Student:
    """representation of a student"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return slef__dict__
        new_dict = []
        for j in attrs:
            try:
                new_dict[j] = self.__dict__[j]
            except FileNotFoundError:
                pass
            return new_dict

        def reload_from_json(self, json):
            """replaces all attributes of the Student instance"""
            for key in json:
                try:
                    setattr(self, key, json[key])
                except FileNotFoundError:
                    pass
