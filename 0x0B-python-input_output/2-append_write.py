#!/usr/bin/python3
"""
contains the append_write function
"""


def append_write(filename="", text=""):
    """returns number ofcharacters added at the end of text file(UTF8)"""
    with open(filename, "a", encoding='utf=8') as f:
        return f.write(text)
