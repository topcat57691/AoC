import requests
import os


def get_input(day_number):
    cookie = os.getenv("AOC_COOKIE")

    if not cookie:
        raise Exception("GIVE ME COOKIES. Environment variable AOC_COOKIE not set")

    url = f"https://adventofcode.com/2023/day/{day_number}/input"
    headers = {"Cookie": cookie}

    res = requests.get(url, headers=headers)
    return res.text
