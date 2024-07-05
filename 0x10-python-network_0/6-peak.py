#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None
    lo, hi = 0, len(list_of_integers) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        # Compare middle element with its right neighbor
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return list_of_integers[lo]
