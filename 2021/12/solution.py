import time
from pathlib import PurePath

# --- Day 12: Passage Pathing ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 12

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        return [x.strip().split("-") for x in file.readlines()]


###############
#  functions  #
###############

def create_cave_system(rough_map):
    cave_system = {}
    for caves in rough_map:
        if caves[0] not in cave_system:
            cave_system[caves[0]] = []
        if caves[1] not in cave_system:
            cave_system[caves[1]] = []
        cave_system[caves[0]].append(caves[1])
        cave_system[caves[1]].append(caves[0])
    return cave_system


def count_paths(cave, been_there, cave_system, small_count=1):
    if cave == "end":
        return 1
    if cave in been_there:
        if cave == "start":
            return 0
        if cave.islower():
            if small_count == 1:
                return 0
            else:
                small_count -= 1
    return sum(count_paths(new_cave, been_there | {cave}, cave_system, small_count) for new_cave in cave_system[cave])


#############
#  answers  #
#############

def get_answer_1(rough_map):
    time_start = time.perf_counter()
    cave_system = create_cave_system(rough_map)
    total = count_paths("start", set(), cave_system)
    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


def get_answer_2(rough_map):
    time_start = time.perf_counter()
    cave_system = create_cave_system(rough_map)
    total = count_paths("start", set(), cave_system, small_count=2)
    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


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
    puzzle_input = parse_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
