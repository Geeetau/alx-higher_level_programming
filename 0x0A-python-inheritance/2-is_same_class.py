#!/usr/bin/python3
"""
contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """returns true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
