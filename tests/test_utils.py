import unittest
from utils.parse import *


class UtilsTest(unittest.TestCase):
    def test_text_to_list(self):
        text = "hello\nworld"
        expected = ["hello", "world"]
        self.assertEqual(text_to_list(text), expected, "Did not return expected list")

    def test_text_to_int_list(self):
        text = "2 3 1\n1 21 3"
        expected = [[2, 3, 1], [1, 21, 3]]
        self.assertEqual(
            text_to_int_list(text), expected, "Did not return expected list"
        )

    def test_text_to_grid(self):
        text = "abc\nhijk\npq"
        expected = [
            ["a", "b", "c"],
            ["h", "i", "j", "k"],
            ["p", "q"],
        ]
        self.assertEqual(
            text_to_grid(text), expected, "Did not return expected list"
        )
