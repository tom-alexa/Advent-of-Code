import time
from pathlib import PurePath

# ---Day 11: Dumbo Octopus  ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 11

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    octopuses = {}
    with open(INPUT_FILE, "r") as file:
        for y, line in enumerate(file.readlines()):
            line = line.strip()
            for x, char in enumerate(line):
                octopuses[(x, y)] = int(char)
    return octopuses


###############
#  functions  #
###############

def add_energy(octopuses, position, flashed, flashes=None):
    if position in flashed:
        return
    if position not in octopuses:
        return
    octopuses[position] += 1
    if not check_octopus(octopuses, position):
        return
    if flashes:
        flashes["total"] += 1
    flashed.add(position)
    x, y = position
    add_energy(octopuses, (x - 1, y - 1), flashed, flashes)
    add_energy(octopuses, (x, y - 1), flashed, flashes)
    add_energy(octopuses, (x + 1, y - 1), flashed, flashes)
    add_energy(octopuses, (x - 1, y), flashed, flashes)
    add_energy(octopuses, (x + 1, y), flashed, flashes)
    add_energy(octopuses, (x - 1, y + 1), flashed, flashes)
    add_energy(octopuses, (x, y + 1), flashed, flashes)
    add_energy(octopuses, (x + 1, y + 1), flashed, flashes)


def check_octopus(octopuses, position):
    if position not in octopuses:
        return False
    if octopuses[position] != 10:
        return False
    octopuses[position] = 0
    return True


#############
#  answers  #
#############

def get_answer_1(octopuses):
    time_start = time.perf_counter()

    octopuses = octopuses.copy()
    flashes = {"total": 0}
    for _ in range(100):
        flashed = set()
        for position in octopuses:
            add_energy(octopuses, position, flashed, flashes)

    time_spent = time.perf_counter() - time_start
    return {"value": flashes["total"], "time": time_spent}


def get_answer_2(octopuses):
    time_start = time.perf_counter()

    octopuses = octopuses.copy()
    step = 0
    while True:
        step += 1
        flashed = set()
        for position in octopuses:
            add_energy(octopuses, position, flashed)
        if len(flashed) >= len(octopuses):
            break

    time_spent = time.perf_counter() - time_start
    return {"value": step, "time": time_spent}


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
    puzzle_input = get_data_from_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
