from utils.parse import text_to_list


def check_is_part(grid, currentRow, currentCol, maxRow, maxCol, ALLOWED_SYMBOLS):
    if currentRow > 0:
        if currentCol > 0:
            if grid[currentRow - 1][currentCol - 1] in ALLOWED_SYMBOLS:
                return currentRow - 1, currentCol - 1

        if currentCol < maxCol:
            if grid[currentRow - 1][currentCol + 1] in ALLOWED_SYMBOLS:
                return currentRow - 1, currentCol + 1

        if grid[currentRow - 1][currentCol] in ALLOWED_SYMBOLS:
            return currentRow - 1, currentCol

    if currentRow < maxRow:
        if currentCol > 0:
            if grid[currentRow + 1][currentCol - 1] in ALLOWED_SYMBOLS:
                return currentRow + 1, currentCol - 1

        if currentCol < maxCol:
            if grid[currentRow + 1][currentCol + 1] in ALLOWED_SYMBOLS:
                return currentRow + 1, currentCol + 1

        if grid[currentRow + 1][currentCol] in ALLOWED_SYMBOLS:
            return currentRow + 1, currentCol

    if currentCol > 0:
        if grid[currentRow][currentCol - 1] in ALLOWED_SYMBOLS:
            return currentRow, currentCol - 1

    if currentCol < maxCol:
        if grid[currentRow][currentCol + 1] in ALLOWED_SYMBOLS:
            return currentRow, currentCol + 1

    return False


def solution_one(problem_input):
    grid = text_to_list(problem_input)
    total = 0
    MAX_ROW_INDEX = len(grid) - 1
    MAX_COL_INDEX = len(grid[0]) - 1
    ALLOWED_SYMBOLS = ["$", "*", "+", "#", "/", "-", "&", "=", "@", "%"]

    for row_index, row in enumerate(grid):
        current_number = ""
        is_part = False
        for col_index, col in enumerate(row):
            if col.isdigit():
                current_number += col

                if not is_part:
                    is_part = (
                        False
                        if check_is_part(
                            grid,
                            row_index,
                            col_index,
                            MAX_ROW_INDEX,
                            MAX_COL_INDEX,
                            ALLOWED_SYMBOLS,
                        )
                        == False
                        else True
                    )
            else:
                if len(current_number) and is_part:
                    total += int(current_number)
                is_part = False
                current_number = ""

        if len(current_number) and is_part:
            total += int(current_number)

    return total


def update_dict(dict, key, number):
    if key in dict:
        dict[key].append(int(number))
    else:
        dict[key] = [int(number)]


def calculate_gear_ratio_sum(dict):
    total = 0
    for value in dict.values():
        if len(value) <= 1:
            continue

        product = 1
        for v in value:
            product *= v

        total += product
    return total


def solution_two(problem_input):
    grid = text_to_list(problem_input)
    total = 0

    MAX_ROW_INDEX = len(grid) - 1
    MAX_COL_INDEX = len(grid[0]) - 1
    ALLOWED_SYMBOLS = ["*"]

    potential_gear_positions = {}
    for row_index, row in enumerate(grid):
        current_number = ""
        found_gear = ""
        is_part = False
        for col_index, col in enumerate(row):
            if col.isdigit():
                current_number += col

                if not is_part:
                    res = check_is_part(
                        grid,
                        row_index,
                        col_index,
                        MAX_ROW_INDEX,
                        MAX_COL_INDEX,
                        ALLOWED_SYMBOLS,
                    )

                    if res != False:
                        gear_row, gear_col = res
                        found_gear = f"{gear_row} {gear_col}"
            else:
                if len(current_number) and len(found_gear):
                    update_dict(potential_gear_positions, found_gear, current_number)
                is_part = False
                current_number = ""
                found_gear = ""

        if len(current_number) and len(found_gear):
            update_dict(potential_gear_positions, found_gear, current_number)

    return calculate_gear_ratio_sum(potential_gear_positions)
