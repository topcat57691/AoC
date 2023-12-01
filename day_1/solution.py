import re
from utils.parse import text_to_list

word_number_lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

word_number_lookup_reversed = {}
for word in word_number_lookup:
    word_number_lookup_reversed[word[::-1]] = word_number_lookup[word]


def get_calibration_value_advanced(line):
    search_string_one = rf"({'|'.join(list(word_number_lookup.keys()))}|\d)"
    search_string_two = rf"({'|'.join(list(word_number_lookup_reversed.keys()))}|\d)"

    first = re.search(search_string_one, line).group()
    last = re.search(search_string_two, line[::-1]).group()

    if not first.isdigit():
        first = word_number_lookup[first]
    if not last.isdigit():
        last = word_number_lookup_reversed[last]

    return int(f"{first}{last}")


def get_calibration_value(line):
    current_char = None

    for char in line:
        if char.isdigit():
            if current_char == None:
                first_char = int(char)

            current_char = int(char)
    return int(f"{first_char}{current_char}")


def solution_one(problem_input):
    parsed = text_to_list(problem_input)
    total = 0

    for line in parsed:
        total += get_calibration_value(line)

    return total


def solution_two(problem_input):
    parsed = text_to_list(problem_input)
    total = 0

    for line in parsed:
        total += get_calibration_value_advanced(line)

    return total
