import unittest
from day_10.solution import *


class Sequences(unittest.TestCase):
    def test_get_start_location(self):
        data_sets = [
            ([["S"]], (0, 0)),
            ([[""]], None),
            ([["T", "S", "T"]], (0, 1)),
            ([["T", "T", "T"], ["T", "S", "T"]], (1, 1)),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                result = get_start_location(data[0])
                self.assertEqual(result, data[1])
