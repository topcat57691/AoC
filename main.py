# main.py
import sys
from dotenv import load_dotenv
from importlib import import_module
from utils.input import *

load_dotenv()


def determine_test_to_run(solution_number):
    if not solution_number:
        return True, True

    if solution_number == 1:
        return True, False

    return False, True


def determine_test_data_sets(real_or_test):
    if not real_or_test:
        return True, True

    if real_or_test == "r":
        return False, True

    return True, False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <day number> [<solution number> <rt>]")
        sys.exit(1)

    day_number = sys.argv[1]
    solution_number = None
    real_or_test = None

    if len(sys.argv) > 2:
        solution_number = int(sys.argv[2])

    if len(sys.argv) > 3:
        real_or_test = sys.argv[3]

    if real_or_test and not real_or_test in ["r", "t"]:
        print("Third argument must be r or t to run (r)eal or (t)est run")
        sys.exit(1)

    run_test_one, run_test_two = determine_test_to_run(solution_number)
    run_fake_test, run_real_test = determine_test_data_sets(real_or_test)

    if run_real_test:
        write_to_input_file(day_number)

    mod = import_module(f"day_{day_number}.solution")
    if run_test_one:
        solution_one = getattr(mod, "solution_one")
    if run_test_two:
        solution_two = getattr(mod, "solution_two")

    if run_fake_test:
        test_input_one = get_test_input(day_number, 1)

        try:
            test_input_two = get_test_input(day_number, 2)
        except:
            test_input_two = get_test_input(day_number, 1)

    if run_real_test:
        real_input = get_real_input(day_number)

    if run_test_one:
        if run_fake_test:
            test_solution_one = solution_one(test_input_one)
            print(f"Test solution 1: {test_solution_one}")
        if run_real_test:
            real_solution_one = solution_one(real_input)
            print(f"Real solution 1: {real_solution_one}")

    if run_test_two:
        if run_fake_test:
            test_solution_two = solution_two(test_input_two)
            print(f"Test solution 2: {test_solution_two}")
        if run_real_test:
            real_solution_two = solution_two(real_input)
            print(f"Real solution 2: {real_solution_two}")
