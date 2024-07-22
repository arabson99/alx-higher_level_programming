#!/usr/bin/python3
"""
	This module adds 2 integers
	and
	returns the addition of the 2 integer
"""
def add_integer(a, b=98):
	"""
		Returns the addition of two integers
	"""
	if not isinstance(a, int) and not isinstance(a, float):
		raise TypeError("a must be an integer")
	elif not isinstance(b, int) and not isinstance(b, float):
		raise TypeError("b must be an integer")
	return int(a) + int(b)
