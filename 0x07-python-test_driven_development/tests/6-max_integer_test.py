#!/usr/bin/python3
"""
	Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Defines unittests for max_integer([..])."""
	
	def test_ordered_list(self):
		"""Test an ordered list of integers."""
		ordered = [1, 2, 3, 4]
		self.assertEqual(max_integer(ordered), 4)

	def test_unordered_list(self):
		"""Test an unordered list of integers."""
		unordered = [1, 4, 2, 3]
		self.assertEqual(max_integer(unordered), 4)

	def test_empty_list(self):
		"""Test an empty list."""
		empty = []
		self.assertEqual(max_integer(empty), None)

	def test_one_element(self):
		"""Test a list with a single element."""
		one_ele = [3]
		self.assertEqual(max_integer(one_ele), 3)

	def test_floats(self):
		"""Test a list of floats."""
		floats = [1.1, 3.3, 2.3, 5.5]
		self.assertEqual(max_integer(floats), 5.5)

	def test_ints_and_floats(self):
		"""Test a list of ints and floats."""
		ints_floats = [1, 2.2, 3.2, 2, 5]
		self.assertEqual(max_integer(ints_floats), 5)

	def test_string(self):
		"""Test a string."""
		string = "Arabson"
		self.assertEqual(max_integer(string), 's')

	def test_list_of_strings(self):
		"""Test a list of strings."""
		strings = ["Arabson", "is", "my", "name"]
		self.assertEqual(max_integer(strings), "name")

	def test_empty_string(self):
		"""Test an empty string."""
		self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
		unittest.main()
