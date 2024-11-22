import unittest

from functions import calculate_sum, string_length, update_dictionary

class TestFunctions(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(3, 5), 8)
        self.assertEqual(calculate_sum(-1, 1), 0)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(-5, -10), -15)

    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length(""), 0)
        self.assertEqual(string_length("a"), 1)
        self.assertEqual(string_length("long string test"), 16)

    def test_update_dictionary(self):
        d = {'a': 1, 'b': 2}
        self.assertEqual(update_dictionary(d, 'a', 3), {'a': 4, 'b': 2})
        self.assertEqual(update_dictionary(d, 'c', 5), {'a': 4, 'b': 2, 'c': 5})
        self.assertEqual(update_dictionary({}, 'x', 10), {'x': 10})

print(calculate_sum(5, 10))  # Output: 15
print(string_length("hello"))  # Output: 5
print(update_dictionary({}, 'key', 100))  # Output: {'key': 100}
