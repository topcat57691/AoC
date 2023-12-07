from enum import Enum
from utils.parse import text_to_list


class HandType(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def character_weight(char):
    char_order = "123456789TJQKA"
    return char_order.index(char)


def get_hand_type(hand):
    dict = {}
    weight = []

    hand = hand.split(" ")[0]

    for card in hand:
        if dict.get(card):
            dict[card] += 1
        else:
            dict[card] = 1
        weight.append(character_weight(card))

    dict_values = list(dict.values())

    if len(dict) == 1:
        # Five of a kind
        return (HandType.FIVE_OF_A_KIND.value, weight)
    if len(dict) == 5:
        # High card
        return (HandType.HIGH_CARD.value, weight)
    if len(dict) == 4:
        # Pair
        return (HandType.PAIR.value, weight)
    if len(dict) == 3:
        # Three of a kind
        if 1 in dict_values and 3 in dict_values:
            return (HandType.THREE_OF_A_KIND.value, weight)
        # Two pair
        return (HandType.TWO_PAIR.value, weight)
    if dict_values[0] == 1 or dict_values[0] == 4:
        # Four of a kind
        return (HandType.FOUR_OF_A_KIND.value, weight)
    # Full house
    return (HandType.FULL_HOUSE.value, weight)


def solution_one(problem_input):
    parsed = text_to_list(problem_input)

    sorted_hands = sorted(parsed, key=get_hand_type)

    total = 0
    for i in range(len(sorted_hands)):
        total += (i + 1) * int(sorted_hands[i].split(" ")[1])
    return total


def solution_two(problem_input):
    print("No solution implemented yet")
    return -1
