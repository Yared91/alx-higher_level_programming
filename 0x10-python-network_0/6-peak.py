#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Handles elements with 1 or 2 elements.
    Gets the middle element
    checks if the middle element is a peak
    looks the peak that is greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    lists = list_of_integers
    start = 0
    last = len(lists)-1

    if lists[start] > lists[start+1]:
        return lists[start]
    if lists[last] > lists[last-1]:
        return lists[last]

    mid = (start+last)//2
    if lists[mid-1] < lists[mid] and lists[mid+1] < lists[mid]:
        return lists[mid]
    if lists[mid] < lists[mid-1]:
        return find_peak(lists[start:mid+1])
    if lists[mid] < lists[mid+1]:
        return find_peak(lists[mid:last+1])
    else:
        return lists[start]
