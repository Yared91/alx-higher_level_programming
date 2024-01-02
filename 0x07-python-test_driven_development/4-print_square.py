#!/usr/bin/python3
"""Describes square printing funtion."""


def print_square(size):
    """Prints a square with the # character."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
