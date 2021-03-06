import time
from pathlib import PurePath

# --- Day 3: Toboggan Trajectory ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 3

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")

JUMP_1 = (3, 1)
JUMPS = {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}


###########
#  input  #
###########

def parse_input():
    grid = []
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            grid.append(line.strip())
    return grid


###############
#  functions  #
###############

def get_tree_encounters(grid, x_jump, y_jump):
    trees = 0
    x = 0
    y = 0
    while y < len(grid):
        line = grid[y]
        if line[x] == "#":
            trees += 1
        x = (x + x_jump) % len(line)
        y += y_jump
    return trees


#############
#  answers  #
#############

def get_answer_1(grid):
    time_start = time.perf_counter()
    trees = get_tree_encounters(grid, JUMP_1[0], JUMP_1[1])
    time_spent = time.perf_counter() - time_start
    return {"value": trees, "time": time_spent}


def get_answer_2(grid):
    time_start = time.perf_counter()
    trees = 1
    for jump in JUMPS:
        trees *= get_tree_encounters(grid, jump[0], jump[1])
    time_spent = time.perf_counter() - time_start
    return {"value": trees, "time": time_spent}


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
