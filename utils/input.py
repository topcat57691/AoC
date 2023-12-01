import os
from utils.fileops import *
from utils.httpclient import get_input

base_dir = os.path.join(os.path.dirname(__file__), "..")


def get_dir_name(day_number):
    return os.path.join(base_dir, f"day_{day_number}")


def get_file_name(day_number, file_name="input"):
    return os.path.join(get_dir_name(day_number), f"{file_name}.txt")


def write_to_input_file(day_number, replace=None):
    file_name = get_file_name(day_number)

    if replace != True and file_exists(file_name):
        return

    text = get_input(day_number)
    write_file(file_name, text)


def get_test_input(day_number, test_number):
    file_name = get_file_name(day_number, f"testInput{test_number}")
    problem_input = read_file(file_name)
    return problem_input.strip()


def get_real_input(day_number):
    file_name = get_file_name(day_number)
    problem_input = read_file(file_name)
    return problem_input.strip()
