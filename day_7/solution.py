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


def character_weight(card, card_precedence="123456789TJQKA"):
    return card_precedence.index(card)


def get_hand_type(frequency_dict):
    dict_values = list(frequency_dict.values())

    if len(frequency_dict) == 1:
        # Five of a kind
        return HandType.FIVE_OF_A_KIND.value
    if len(frequency_dict) == 5:
        # High card
        return HandType.HIGH_CARD.value
    if len(frequency_dict) == 4:
        # Pair
        return HandType.PAIR.value
    if len(frequency_dict) == 3:
        # Three of a kind
        if 1 in dict_values and 3 in dict_values:
            return HandType.THREE_OF_A_KIND.value
        # Two pair
        return HandType.TWO_PAIR.value
    if dict_values[0] == 1 or dict_values[0] == 4:
        # Four of a kind
        return HandType.FOUR_OF_A_KIND.value
    # Full house
    return HandType.FULL_HOUSE.value


def get_hand_card_scores(hand, with_wildcards=False):
    frequencies = {}
    weight = []

    hand_cards = hand.split(" ")[0]

    for card in hand_cards:
        if with_wildcards:
            weight.append(character_weight(card, "J123456789TQKA"))

            if card == "J":
                continue
        else:
            weight.append(character_weight(card))

        if frequencies.get(card):
            frequencies[card] += 1
        else:
            frequencies[card] = 1

    if with_wildcards and "J" in hand_cards:

        def sort_by_value(dict):
            return dict[1]

        if hand_cards == "JJJJJ":
            return {"J": 5}, weight

        most_common = sorted(
            list(frequencies.items()), key=sort_by_value, reverse=True
        )[0][0]

        best_hand = hand.replace("J", str(most_common))
        frequencies = get_hand_card_scores(best_hand)[0]
    return frequencies, weight


def get_card_sort_order_with_wildcards(hand):
    frequencies, weight = get_hand_card_scores(hand, True)
    hand_type = get_hand_type(frequencies)
    return hand_type, weight


def get_card_sort_order(hand):
    frequencies, weight = get_hand_card_scores(hand)
    hand_type = get_hand_type(frequencies)
    return hand_type, weight


def solution_one(problem_input):
    parsed = text_to_list(problem_input)

    sorted_hands = sorted(parsed, key=get_card_sort_order)

    total = 0
    for i in range(len(sorted_hands)):
        total += (i + 1) * int(sorted_hands[i].split(" ")[1])
    return total


def solution_two(problem_input):
    parsed = text_to_list(problem_input)

    sorted_hands = sorted(parsed, key=get_card_sort_order_with_wildcards)

    total = 0
    for i in range(len(sorted_hands)):
        total += (i + 1) * int(sorted_hands[i].split(" ")[1])
    return total
