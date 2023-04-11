#!/usr/bin/python3
"""
contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """True if the object is an instance of a class otherwise False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
