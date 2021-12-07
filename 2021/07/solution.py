import time
from pathlib import PurePath

# --- Day 7: The Treachery of Whales ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 7

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        return [int(number) for number in file.read().split(",")]


###############
#  functions  #
###############

def least_fuel(position, fuel_growth=False):
    minimal = min(position)
    maximal = max(position)
    best = float("inf")
    for new in range(minimal, maximal + 1):
        current = 0
        for pos in position:
            change = abs(pos - new)
            if fuel_growth:
                change += ((change - 1) * 0.5 * change)
            current += change
        best = min(best, current)
    return int(best)


#############
#  answers  #
#############

def get_answer_1(position):
    time_start = time.perf_counter()
    fuel_cost = least_fuel(position)
    time_spent = time.perf_counter() - time_start
    return {"value": fuel_cost, "time": time_spent}


def get_answer_2(position):
    time_start = time.perf_counter()
    fuel_cost = least_fuel(position, fuel_growth=True)
    time_spent = time.perf_counter() - time_start
    return {"value": fuel_cost, "time": time_spent}


###########
#  print  #
###########

def print_answers(answer_1, answer_2):
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"], 3)
    answer_2_time = round(answer_2["time"], 3)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    length_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    length_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indentation = " " * 2
    print(f"\n{indentation}{YEAR} > {DAY}")
    print(f"{indentation*2}Answer 1: {answer_1_value}{length_to_add_1} | {answer_1_time:.3f} s")
    print(f"{indentation*2}Answer 2: {answer_2_value}{length_to_add_2} | {answer_2_time:.3f} s\n")


##########
#  main  #
##########

def main():
    puzzle_input = get_data_from_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
