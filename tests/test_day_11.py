import unittest
from day_11.solution import *
from utils.parse import text_to_grid


class Galaxies(unittest.TestCase):
    def test_get_empty_lines(self):
        data_sets = [
            ("....#..", {"cols": [0, 1, 2, 3, 5, 6], "rows": []}),
            ("..#..\n#....\n.#...", {"cols": [3, 4], "rows": []}),
            (".#..\n#.#.\n....", {"cols": [3], "rows": [2]}),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                parsed = text_to_grid(data[0])
                result = get_empty_lines(parsed)
                self.assertEqual(result, data[1])

    def test_expand_universe(self):
        data_sets = [
            ("#", "#"),
            ("...", "......\n......"),
            (".#.", "..#.."),
            ("..\n.#", "...\n...\n..#"),
            (
                ".....\n.#.#.\n...#.\n.....\n...#.\n.....",
                "........\n........\n..#..#..\n.....#..\n........\n........\n.....#..\n........\n........",
            ),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                parsed = text_to_grid(data[0])
                expected = text_to_grid(data[1])
                result = expand_universe(parsed, get_empty_lines(parsed))
                self.assertEqual(result, expected)

    def test_map_galaxies(self):
        data_sets = [
            ("#", [(0, 0)]),
            ("...", []),
            (".#.", [(0, 1)]),
            ("..\n.#", [(1, 1)]),
            (
                ".....\n.#.#.\n...#.\n.....\n...#.\n.....",
                [(1, 1), (1, 3), (2, 3), (4, 3)],
            ),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                parsed = text_to_grid(data[0])
                result = map_galaxies(parsed)
                self.assertEqual(result, data[1])

    def test_get_shortest_route(self):
        data_sets = [
            ((0, 0), (0, 0), 0),
            ((0, 0), (0, 1), 1),
            ((0, 0), (1, 1), 2),
            ((174, 362), (92, 468), 188),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                result = get_shortest_route(data[0], data[1])
                self.assertEqual(result, data[2])

    def test_count_route_expansion_intersections(self):
        data_sets = [
            ((0, 0), (0, 0), {"rows": [], "cols": []}, 0),
            ((0, 0), (0, 1), {"rows": [], "cols": []}, 0),
            ((0, 0), (1, 1), {"rows": [], "cols": []}, 0),
            ((0, 0), (2, 2), {"rows": [1], "cols": [1]}, 2),
            ((0, 0), (2, 2), {"rows": [], "cols": [1]}, 1),
            (
                (174, 362),
                (92, 468),
                {"rows": [93, 94, 95, 96, 97], "cols": [400, 401, 402]},
                8,
            ),
        ]

        for data in data_sets:
            with self.subTest(data=data):
                result = count_route_expansion_intersections(data[0], data[1], data[2])
                self.assertEqual(result, data[3])
