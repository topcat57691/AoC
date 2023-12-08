from collections import deque
from math import lcm


def parse_input(problem_input):
    instructions, raw_nodes = problem_input.split("\n\n")

    nodes = {}
    for node in raw_nodes.split("\n"):
        current, next = node.split(" = ")
        nodes[current] = next.replace("(", "").replace(")", "").split(", ")

    instructions = deque([*instructions])

    return instructions, nodes


def solution_one(problem_input):
    instructions, nodes = parse_input(problem_input)

    current_node = "AAA"
    moves = 0
    while current_node != "ZZZ":
        direction = 0 if instructions[0] == "L" else 1
        current_node = nodes[current_node][direction]

        instructions.rotate(-1)
        moves += 1
    return moves


def traverse(start_node, instructions, nodes):
    current_node = start_node
    moves = 0
    while not current_node.endswith("Z"):
        direction = 0 if instructions[0] == "L" else 1
        current_node = nodes[current_node][direction]

        instructions.rotate(-1)
        moves += 1
    return moves


def solution_two(problem_input):
    instructions, nodes = parse_input(problem_input)
    start_nodes = [node for node in nodes if node.endswith("A")]

    moves_list = [traverse(node, instructions, nodes) for node in start_nodes]
    return lcm(*moves_list)
