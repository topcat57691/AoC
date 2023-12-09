from utils.parse import text_to_int_list


def get_diffs(nums):
    return [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]


def traverse(nums):
    diffs = get_diffs(nums)

    if all(v == 0 for v in nums):
        return 0
    else:
        new_diffs = traverse(diffs)
        return nums[-1] + new_diffs


def solution_one(problem_input):
    parsed = text_to_int_list(problem_input)
    return sum([traverse(num_arr) for num_arr in parsed])


def solution_two(input):
    return sum([traverse(num_arr) for num_arr in input])
