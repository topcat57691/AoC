from utils.parse import text_to_list
import re

cubes_in_bag = {"red": 12, "green": 13, "blue": 14}


def parse_cube(str):
    number = re.search(r"\d+", str).group()
    colour = re.search(r"red|green|blue", str).group()
    return colour, int(number)


def sum_of_possible_games(list):
    total = 0

    for input in list:
        key, *games = re.split(r"[:;,]", input)
        key = re.search(r"\d+", key).group()
        possible = True

        for game in games:
            colour, number = parse_cube(game)
            if number > cubes_in_bag[colour]:
                possible = False
                break

        if possible:
            total += int(key)

    return total


def sum_of_game_powers(list):
    total = 0

    for input in list:
        key, *games = re.split(r"[:;,]", input)
        key = re.search(r"\d+", key).group()

        rgb = {"red": 0, "green": 0, "blue": 0}
        for game in games:
            colour, number = parse_cube(game)

            rgb[colour] = max(rgb[colour], number)

        total += rgb["red"] * rgb["green"] * rgb["blue"]

    return total


def solution_one(problem_input):
    list = text_to_list(problem_input)
    return sum_of_possible_games(list)


def solution_two(problem_input):
    list = text_to_list(problem_input)
    return sum_of_game_powers(list)
