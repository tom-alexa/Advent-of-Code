import time
from pathlib import PurePath

# --- Day 10: Adapter Array ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 10

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        return [ int(line.strip()) for line in file.readlines() ]


###############
#  functions  #
###############

def multiple(array_counter):
    power = max(0, array_counter - 2)
    reducer = get_reducer(power, 0) if power >= 3 else 0
    return 2**power - reducer


def get_reducer(power, reducer):
    reducer += 2**(power - 3)
    return get_reducer(power - 1, reducer) if (power - 1) >= 3 else reducer


#############
#  answers  #
#############

def get_answer_1(adapters):
    time_start = time.perf_counter()
    adapters = sorted(adapters)
    joltage = {"adapters": {"joltage": adapters, "min": adapters[0], "max": adapters[-1]}, "device": adapters[-1] + 3, "differences": {1: 0, 2: 0, 3: 0}}
    last = 0
    for adapter in adapters:
        joltage["differences"][adapter - last] += 1
        last = adapter
    joltage["differences"][joltage["device"] - last] += 1
    time_spent = time.perf_counter() - time_start
    return {"value": joltage["differences"][1] * joltage["differences"][3], "time": time_spent}


def get_answer_2(adapters):
    time_start = time.perf_counter()
    adapters = sorted(adapters)
    option = {"ways": 1, "device": adapters[-1] + 3}

    array_counter = 0
    last_number = 0
    for number in [0] + adapters + [option["device"]]:
        if last_number + 3 <= number:
            option["ways"] *= multiple(array_counter)
            array_counter = 0
        array_counter += 1
        last_number = number
    option["ways"] *= multiple(array_counter)

    time_spent = time.perf_counter() - time_start
    return {"value": option["ways"], "time": time_spent}


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
