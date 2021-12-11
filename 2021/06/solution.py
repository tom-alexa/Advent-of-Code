import time
from pathlib import PurePath
from collections import Counter

# --- Day 6: Lanternfish ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 6

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        return dict(Counter([int(number) for number in file.read().split(",")]))


###############
#  functions  #
###############

def growth(initial_state, days):
    list_of_lanternfish = initial_state.copy()
    for _ in range(days):
        new_fish = {i: 0 for i in range(9)}
        for timer, count in list_of_lanternfish.items():
            timer -= 1
            if timer < 0:
                new_fish[8] += count
                timer = 6
            new_fish[timer] += count
        list_of_lanternfish = new_fish.copy()
    return sum(list_of_lanternfish.values())


#############
#  answers  #
#############

def get_answer_1(initial_state):
    time_start = time.perf_counter()
    total = growth(initial_state, 80)
    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


def get_answer_2(initial_state):
    time_start = time.perf_counter()
    total = growth(initial_state, 256)
    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


###########
#  print  #
###########

def print_answers(answer_1, answer_2):
    to_milliseconds = 1000
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"] * to_milliseconds, 3)
    answer_2_time = round(answer_2["time"] * to_milliseconds, 3)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    length_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    length_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indentation = " " * 2
    print(f"\n{indentation}{YEAR} > {DAY}")
    print(f"{indentation*2}Answer 1: {answer_1_value}{length_to_add_1} | {answer_1_time:.3f} ms")
    print(f"{indentation*2}Answer 2: {answer_2_value}{length_to_add_2} | {answer_2_time:.3f} ms\n")


##########
#  main  #
##########

def main():
    puzzle_input = parse_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
