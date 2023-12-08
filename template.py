import sys
import os

from distutils.dir_util import copy_tree

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup.py <day number>")
        sys.exit(1)

    day_number = sys.argv[1]
    dir_name = f"day_{day_number}"

    if os.path.isdir(dir_name):
        print(f"/{dir_name} exists. Exiting")
        sys.exit(1)

    copy_tree("template", f"day_{day_number}")
