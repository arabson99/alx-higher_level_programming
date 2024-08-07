#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in list_of_integers using a binary search approach"""

    if not list_of_integers:
        return None
    def binary_search_peak(nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            return binary_search_peak(nums, mid + 1, high)
        else:
            return binary_search_peak(nums, low, mid)
    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
