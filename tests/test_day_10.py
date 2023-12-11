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

    # def test_get_next_term(self):
    #     def get_next_term(nums, diffs):
    #         return nums[-1] + diffs

    #     def get_previous_term(nums, diffs):
    #         return nums[0] - diffs

    #     data_sets = [
    #         ([1, 2, 3, 4, 5], get_next_term, 6),
    #         ([1, 1, 1, 1, 1], get_next_term, 1),
    #         ([1, 8, 27, 64], get_next_term, 125),
    #         ([1, 2, 3, 4, 5], get_previous_term, 0),
    #         ([1, 1, 1, 1, 1], get_previous_term, 1),
    #         ([27, 64, 125, 216], get_previous_term, 8),
    #     ]

    #     for data in data_sets:
    #         with self.subTest(data=data):
    #             result = traverse(data[0], data[1])
    #             self.assertEqual(result, data[2])
