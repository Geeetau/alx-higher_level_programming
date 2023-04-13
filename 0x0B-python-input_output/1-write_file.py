#!/usr/bin/python3
"""
contains the write_file function
"""


def write_file(filename="", text=""):
    """writes string to a text file(UTF8) and returns the number of char"""
    with open(filename, "w", encoding='utf=8') as f:
        return f.write(text)
