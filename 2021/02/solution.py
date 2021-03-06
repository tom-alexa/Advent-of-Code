import time
from pathlib import PurePath

# --- Day 2: Dive! ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 2

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        return list(map(dictionary, file.readlines()))


###############
#  functions  #
###############

def dictionary(line):
    direction, length = line.strip().split(" ")
    length = int(length)
    return {"direction": direction, "length": length}


#############
#  answers  #
#############

def get_answer_1(moves):
    time_start = time.perf_counter()

    position = {"horizontal": 0, "depth": 0}
    for move in moves:
        if move["direction"] == "forward":
            position["horizontal"] += move["length"]
        elif move["direction"] == "down":
            position["depth"] += move["length"]
        elif move["direction"] == "up":
            position["depth"] -= move["length"]
    multiply = position["horizontal"] * position["depth"]

    time_spent = time.perf_counter() - time_start
    return {"value": multiply, "time": time_spent}


def get_answer_2(moves):
    time_start = time.perf_counter()

    position = {"horizontal": 0, "depth": 0, "aim": 0}
    for move in moves:
        if move["direction"] == "forward":
            position["horizontal"] += move["length"]
            position["depth"] += (move["length"] * position["aim"])
        elif move["direction"] == "down":
            position["aim"] += move["length"]
        elif move["direction"] == "up":
            position["aim"] -= move["length"]
    multiply = position["horizontal"] * position["depth"]

    time_spent = time.perf_counter() - time_start
    return {"value": multiply, "time": time_spent}


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
