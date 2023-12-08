import unittest
from day_7.solution import get_hand_type


class CardHand(unittest.TestCase):
    def test_high_card(self):
        self.assertEqual(
            get_hand_type({"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1}),
            0,
            "Returned the wrong hand type",
        )

    def test_pair(self):
        self.assertEqual(
            get_hand_type({"A": 1, "K": 2, "J": 1, "T": 1}),
            1,
            "Returned the wrong hand type",
        )

    def test_two_pair(self):
        self.assertEqual(
            get_hand_type({"K": 2, "Q": 1, "J": 2}),
            2,
            "Returned the wrong hand type",
        )

    def test_three_of_a_kind(self):
        self.assertEqual(
            get_hand_type({"A": 1, "K": 1, "Q": 3}),
            3,
            "Returned the wrong hand type",
        )

    def test_full_house(self):
        self.assertEqual(
            get_hand_type({"A": 2, "K": 3}),
            4,
            "Returned the wrong hand type",
        )

    def test_four_of_a_kind(self):
        self.assertEqual(
            get_hand_type({"A": 1, "K": 4}),
            5,
            "Returned the wrong hand type",
        )

    def test_five_of_a_kind(self):
        self.assertEqual(
            get_hand_type({"A": 5}),
            6,
            "Returned the wrong hand type",
        )
