import unittest
from day_9.solution import *


class Sequences(unittest.TestCase):
    def test_get_diffs(self):
        data_sets = [
            ([1, 2, 3, 4, 5], [1, 1, 1, 1]),
            ([1, 1, 1, 1, 1], [0, 0, 0, 0]),
            ([1, 2, 4, 8, 16, 32], [1, 2, 4, 8, 16]),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                result = get_diffs(data[0])
                self.assertEqual(result, data[1])

    def test_get_next_term(self):
        data_sets = [
            ([1, 2, 3, 4, 5], 6),
            ([1, 1, 1, 1, 1], 1),
            ([1, 8, 27, 64], 125),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                result = traverse(data[0])
                self.assertEqual(result, data[1])
