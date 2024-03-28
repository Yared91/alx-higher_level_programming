#!/usr/bin/python3
"""
Definition of peak algorithm.
"""


def find_peak(list_of_integers):
    """
    defines the find_peak function.
    """
    if len(list_of_integers) == 0:
        return None

    count = list_of_integers
    begin = 0
    end = len(count)-1

    if count[begin] > count[begin+1]:
        return count[begin]
    if count[end] > count[end-1]:
        return count[end]

    mid = (begin+end)//2
    if count[mid-1] < count[mid] and count[mid+1] < count[mid]:
        return count[mid]
    if count[mid] < count[mid-1]:
        return find_peak(count[begin:mid+1])
    if count[mid] < count[mid+1]:
        return find_peak(count[mid:end+1])
    else:
        return count[begin]
