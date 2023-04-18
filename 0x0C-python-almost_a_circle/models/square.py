#!/usr/bin/python3
"""
This module contains the "Square" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

     @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width
