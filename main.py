# main.py
import sys
from dotenv import load_dotenv
from importlib import import_module
from utils.input import *

load_dotenv()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day number>")
        sys.exit(1)

    day_number = sys.argv[1]

    write_to_input_file(day_number)

    mod = import_module(f"day_{day_number}.solution")
    solution_one = getattr(mod, "solution_one")
    solution_two = getattr(mod, "solution_two")

    test_input_one = get_test_input(day_number, 1)

    try:
        test_input_two = get_test_input(day_number, 2)
    except:
        test_input_two = get_test_input(day_number, 1)

    real_input = get_real_input(day_number)

    test_solution_one = solution_one(test_input_one)
    real_solution_one = solution_one(real_input)
    test_solution_two = solution_two(test_input_two)
    real_solution_two = solution_two(real_input)

    print(f"Test solution 1: {test_solution_one}")
    print(f"Real solution 1: {real_solution_one}")
    print(f"Test solution 2: {test_solution_two}")
    print(f"Real solution 2: {real_solution_two}")
