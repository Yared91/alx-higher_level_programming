#!/usr/bin/python3
"""
Definition of a peak-finding algorithm.
"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    count = len(list_of_integers)
    if count == 1:
        return list_of_integers[0]
    elif count == 2:
        return max(list_of_integers)

    medium = int(size / 2)
    top = list_of_integers[medium]
    if top > list_of_integers[medium - 1] and top > list_of_integers[medium + 1]:
        return top
    elif top < list_of_integers[medium - 1]:
        return find_peak(list_of_integers[:medium])
    else:
        return find_peak(list_of_integers[medium + 1:])
