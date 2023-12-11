import math
from enum import Enum
from utils.parse import text_to_grid


class DIRECTIONS(Enum):
    START = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


UP_VECTOR = (0, -1, DIRECTIONS.UP)
DOWN_VECTOR = (0, 1, DIRECTIONS.DOWN)
LEFT_VECTOR = (-1, 0, DIRECTIONS.LEFT)
RIGHT_VECTOR = (1, 0, DIRECTIONS.RIGHT)


class PipeNode:
    def __init__(self, distance_from_origin, row, col, pipe, direction, route_id=0):
        self.distance_from_origin = distance_from_origin
        self.row = row
        self.col = col
        self.pipe = pipe
        self.entry_direction = direction
        self.id = route_id

    def get_direction_vector(self):
        if self.pipe == "S":
            if self.entry_direction == DIRECTIONS.UP:
                return UP_VECTOR
            if self.entry_direction == DIRECTIONS.DOWN:
                return DOWN_VECTOR
            if self.entry_direction == DIRECTIONS.LEFT:
                return LEFT_VECTOR
            if self.entry_direction == DIRECTIONS.RIGHT:
                return RIGHT_VECTOR

        if self.pipe == "|":
            if self.entry_direction == DIRECTIONS.UP:
                return UP_VECTOR
            elif self.entry_direction == DIRECTIONS.DOWN:
                return DOWN_VECTOR

        if self.pipe == "-":
            if self.entry_direction == DIRECTIONS.LEFT:
                return LEFT_VECTOR
            elif self.entry_direction == DIRECTIONS.RIGHT:
                return RIGHT_VECTOR

        if self.pipe == "F":
            if self.entry_direction == DIRECTIONS.UP:
                return RIGHT_VECTOR
            elif self.entry_direction == DIRECTIONS.LEFT:
                return DOWN_VECTOR

        if self.pipe == "J":
            if self.entry_direction == DIRECTIONS.RIGHT:
                return UP_VECTOR
            elif self.entry_direction == DIRECTIONS.DOWN:
                return LEFT_VECTOR

        if self.pipe == "L":
            if self.entry_direction == DIRECTIONS.DOWN:
                return RIGHT_VECTOR
            elif self.entry_direction == DIRECTIONS.LEFT:
                return UP_VECTOR

        if self.pipe == "7":
            if self.entry_direction == DIRECTIONS.RIGHT:
                return DOWN_VECTOR
            elif self.entry_direction == DIRECTIONS.UP:
                return LEFT_VECTOR

        print("Nope", self.pipe, self.entry_direction)
        return None

    def get_next(self, grid):
        height = len(grid)
        width = len(grid[0])

        vector = self.get_direction_vector()
        if vector == None:
            return None
        col_change, row_change, new_direction = vector
        new_col = self.col + col_change
        new_row = self.row + row_change

        if new_col < 0 or new_col >= width or new_row < 0 or new_row >= height:
            return None

        return PipeNode(
            self.distance_from_origin + 1,
            new_row,
            new_col,
            grid[new_row][new_col],
            new_direction,
            self.id,
        )


def get_start_location(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                return row, col


def solution_one(problem_input):
    grid = text_to_grid(problem_input)
    row, col = get_start_location(grid)
    queue = []
    for direction in [
        DIRECTIONS.UP,
        DIRECTIONS.LEFT,
        DIRECTIONS.DOWN,
        DIRECTIONS.RIGHT,
    ]:
        new_node = PipeNode(0, row, col, "S", direction).get_next(grid)
        if new_node != None:
            queue.append(new_node)

    while True:
        node = queue.pop(0)
        if node.pipe == "S":
            break

        new_node = node.get_next(grid)
        if new_node != None:
            queue.append(new_node)

    total_distance = queue[0].distance_from_origin
    return math.ceil(total_distance / 2)


def solution_two(problem_input):
    grid = text_to_grid(problem_input)
    row, col = get_start_location(grid)
    queue = []
    for direction in [
        (DIRECTIONS.UP, 0),
        (DIRECTIONS.LEFT, 1),
        (DIRECTIONS.DOWN, 2),
        (DIRECTIONS.RIGHT, 3),
    ]:
        new_node = PipeNode(0, row, col, "S", direction[0], direction[1]).get_next(grid)
        if new_node != None:
            queue.append(new_node)

    i = 0
    while True and i < len(queue):
        node = queue[i]
        if node.pipe == "S":
            break

        new_node = node.get_next(grid)
        if new_node != None:
            queue.append(new_node)
        i += 1

    route_id = queue[-1].id
    filtered = [p for p in queue if p.id == route_id]
    route_coordinates = [(p.col, p.row) for p in filtered]
    route_coordinates.append((col, row))

    # Need to figure out what piece S effectively acts as
    before_start, on_start = filtered[-2:]
    after_start = filtered[0]

    effective_starting_pipe = "S"
    if before_start.pipe == "L" and after_start.entry_direction == DIRECTIONS.DOWN:
        effective_starting_pipe = "7"
    if before_start.pipe == "F" and after_start.entry_direction == DIRECTIONS.UP:
        effective_starting_pipe = "J"

    inside = False
    tiles = 0
    previous_intersection = None
    DEBUG = 5

    draw_it = ""
    draw_it_raw = ""
    # for row in range(DEBUG):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pipe = grid[row][col]
            if pipe == "S":
                draw_it += "S"
                draw_it_raw += "S"
            elif (col, row) in route_coordinates:
                draw_it += pipe
                draw_it_raw += "x"
            else:
                draw_it += "."
                draw_it_raw += "."

            if (
                pipe == "-"
                or (previous_intersection == "F" and pipe == "J")
                or (previous_intersection == "L" and pipe == "7")
            ) and (col, row) in route_coordinates:
                continue

                # previous_intersection = None

            if (col, row) in route_coordinates:
                inside = not inside
                previous_intersection = pipe
            elif inside:
                tiles += 1
        inside = False
        draw_it += "\n"
        draw_it_raw += "\n"
    print(draw_it)
    print(draw_it_raw)
    return tiles


# working
# S="data"
# P="input.txt"
# with open(P,"r") as f:
# 	R=f.read()
# G=R.split("\n")
# H=len(G)
# W=len(G[0])

# O = [[0]*W for _ in range(H)] # part 2

# ax = -1
# ay = -1
# for i in range(H):
# 	for j in range(W):
# 		if "S" in G[i]:
# 			ax=i
# 			ay=G[i].find("S")
# print(ax,ay)

# # rightward downward leftward upward
# dirs = [(0,1),(1,0),(0,-1),(-1,0)]
# happy = ["-7J", "|LJ", "-FL", "|F7"]
# Sdirs = []
# for i in range(4):
# 	pos = dirs[i]
# 	bx = ax+pos[0]
# 	by = ay+pos[1]
# 	if bx>=0 and bx<=H and by>=0 and by<=W and G[bx][by] in happy[i]:
# 		Sdirs.append(i)
# print(Sdirs)
# Svalid = 3 in Sdirs # part 2

# # rightward downward leftward upward
# transform = {
# 	(0,"-"): 0,
# 	(0,"7"): 1,
# 	(0,"J"): 3,
# 	(2,"-"): 2,
# 	(2,"F"): 1,
# 	(2,"L"): 3,
# 	(1,"|"): 1,
# 	(1,"L"): 0,
# 	(1,"J"): 2,
# 	(3,"|"): 3,
# 	(3,"F"): 0,
# 	(3,"7"): 2,
# }

# curdir = Sdirs[0]
# cx = ax + dirs[curdir][0]
# cy = ay + dirs[curdir][1]
# ln = 1
# O[ax][ay] = 1 # Part 2
# while (cx,cy)!=(ax,ay):
# 	O[cx][cy] = 1 # Part 2
# 	ln += 1
# 	curdir = transform[(curdir,G[cx][cy])]
# 	cx = cx + dirs[curdir][0]
# 	cy = cy + dirs[curdir][1]
# print(ln)
# print(ln//2)

# # End Part 1
# # Begin Part 2

# ct = 0
# for i in range(H):
# 	inn = False
# 	for j in range(W):
# 		if O[i][j]:
# 			if G[i][j] in "|JL" or (G[i][j]=="S" and Svalid): inn = not inn
# 		else:
# 			ct += inn
# print(ct)
