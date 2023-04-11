#!/usr/bin/python3
"""
contains a full rectangle
"""


class BaseGeometry:
    """a class with a public instance methods area and integer_validator"""
    def area(self):
        """ raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        raise TypeError("{:s} must be an integer".format(name))
    if value <= 0:
        raie ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """a representation of a rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
