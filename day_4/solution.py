from utils.parse import text_to_list
import re


def count_winners(line):
    winning_numbers, my_numbers = line.split(":")[1].strip().split(" | ")
    winning_numbers = winning_numbers.split(" ")
    my_numbers = my_numbers.split(" ")
    winners = 0
    for number in my_numbers:
        if number.strip() and number.strip() in winning_numbers:
            winners += 1

    return winners


def sum_winning_numbers(parsed):
    total = 0
    for line in parsed:
        winners = count_winners(line)

        if winners:
            total += 2 ** (winners - 1)

    return total


def count_copies(parsed):
    mydict = {0: 1}
    total = 0
    for line in parsed:
        id = int(re.search(r"\d+", line).group()) - 1
        winners = count_winners(line)

        if not mydict.get(id):
            mydict[id] = 1

        number_of_copies = mydict.get(id)

        if winners:
            for i in range(winners):
                if not mydict.get(id + i + 1):
                    mydict[id + i + 1] = 1

                mydict[id + i + 1] += number_of_copies
        total += number_of_copies
        number_of_copies = 0
    return total


# Close attempt to use a queue instead - thought it would be fun, it goes wrong around 11, where it's out by 1
# def count_copies(parsed):
#     total = 0
#     queue = [0]
#     for line in parsed:
#         winners = count_winners(line)

#         if len(queue):
#             number_of_duplicates = queue.pop(0)

#         if winners:
#             for i in range(winners):
#                 if len(queue) >= i + 1:
#                     queue[i] += 1 + number_of_duplicates
#                 else:
#                     queue.insert(i, 1)

#         # print(number_of_duplicates, winners, line)
#         total += number_of_duplicates + 1
#         number_of_duplicates = 0
#     return total


def solution_one(problem_input):
    parsed = text_to_list(problem_input)

    return sum_winning_numbers(parsed)


def solution_two(problem_input):
    parsed = text_to_list(problem_input)

    return count_copies(parsed)
