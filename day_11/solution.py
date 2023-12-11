from utils.parse import text_to_grid
import math


def get_empty_lines(universe):
    empty = {"cols": list(range(len(universe[0]))), "rows": list(range(len(universe)))}

    for row, line in enumerate(universe):
        for col, space in enumerate(line):
            if space == "#":
                if row in empty["rows"]:
                    empty["rows"].remove(row)
                if col in empty["cols"]:
                    empty["cols"].remove(col)
    return empty


def expand_universe(universe, empty_lines):
    new_universe = []

    for i_row, line in enumerate(universe):
        new_row = []
        for i_col, space in enumerate(line):
            new_row.append(space)
            if i_col in empty_lines["cols"]:
                new_row.append(space)
        new_universe.append(new_row)
        if i_row in empty_lines["rows"]:
            new_universe.append(new_row)

    return new_universe


def map_galaxies(universe):
    galaxies = []

    for row in range(len(universe)):
        for col in range(len(universe[0])):
            if universe[row][col] == "#":
                galaxies.append((row, col))

    return galaxies


def get_shortest_route(point_a, point_b):
    return abs(point_b[0] - point_a[0]) + abs(point_b[1] - point_a[1])


def count_route_expansion_intersections(point_a, point_b, empty_lines):
    intersections = 0

    for row in empty_lines["rows"]:
        if min(point_a[0], point_b[0]) < row < max(point_a[0], point_b[0]):
            intersections += 1
    for col in empty_lines["cols"]:
        if min(point_a[1], point_b[1]) < col < max(point_a[1], point_b[1]):
            intersections += 1
    return intersections


def solution_one(problem_input):
    parsed = text_to_grid(problem_input)
    empties = get_empty_lines(parsed)
    universe = expand_universe(parsed, empties)
    galaxies = map_galaxies(universe)

    sum_shortest = 0

    while galaxies:
        galaxy = galaxies.pop()
        sum_shortest += sum([get_shortest_route(galaxy, s) for s in galaxies])

    return sum_shortest


def solution_two(problem_input):
    expansion_factor = 1000000
    universe = text_to_grid(problem_input)
    empties = get_empty_lines(universe)
    galaxies = map_galaxies(universe)

    sum_shortest = 0

    while galaxies:
        current_galaxy = galaxies.pop()

        for galaxy in galaxies:
            shortest = get_shortest_route(current_galaxy, galaxy)
            intersections = count_route_expansion_intersections(
                current_galaxy, galaxy, empties
            )
            sum_shortest += shortest + (expansion_factor - 1) * intersections

    return sum_shortest
