#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(b, c).
"""


def add_integer(b, c):
    """Return the addition of two numbers."""
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(c) is not int and type(c) is not float:
        raise TypeError("c must be an integer")
    if type(b) is float:
        a = int(a)
    if type(c) is float:
        c = int(c)
    return b + c
