def calculate_winning_combinations(time, target_distance):
    winning_combinations = 0
    for i in range(1, time):
        if (i * (time - i)) > target_distance:
            winning_combinations += 1
        elif winning_combinations:
            break
    return winning_combinations


def solution_one(problem_input):
    time, distance = problem_input.split("\n")
    time = list(map(int, time.split(":")[1].split()))
    distance = list(map(int, distance.split(":")[1].split()))

    total = 1
    for i in range(len(time)):
        combinations = calculate_winning_combinations(time[i], distance[i])
        if combinations:
            total *= combinations

    return total


def solution_two(problem_input):
    time, distance = problem_input.split("\n")

    time = int(time.split(":")[1].replace(" ", ""))
    distance = int(distance.split(":")[1].replace(" ", ""))
    combinations = calculate_winning_combinations(time, distance)

    return combinations
