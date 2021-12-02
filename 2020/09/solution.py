import time
from pathlib import PurePath

# --- Day 9: Encoding Error ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 9

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")

PREAMBLE_LENGTH = 25


###########
#  input  #
###########

def get_data_from_input():
    numbers = []
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            number = int(line.strip())
            numbers.append(number)
    return numbers


###############
#  functions  #
###############

def is_valid(number, preamble):
    for first_preamble_number in preamble:
        for second_preamble_number in preamble:
            if number == first_preamble_number + second_preamble_number:
                return True
    return False


def get_invalid_number(numbers):
    preamble = numbers[:PREAMBLE_LENGTH]
    for number in numbers[PREAMBLE_LENGTH:]:
        if not is_valid(number, preamble):
            return number
        preamble = preamble[1:]
        preamble.append(number)


def add_number(added_numbers, numbers):
    added_numbers["index"]["max"] += 1
    new_number = numbers[added_numbers["index"]["max"]]
    added_numbers["numbers"].append(new_number)
    added_numbers["sum"] += new_number
    if new_number < added_numbers["value"]["min"]:
        added_numbers["value"]["min"] = new_number
    elif new_number > added_numbers["value"]["max"]:
        added_numbers["value"]["max"] = new_number


def remove_number(added_numbers, numbers):
    added_numbers["sum"] -= numbers[added_numbers["index"]["min"]]
    added_numbers["index"]["min"] += 1
    added_numbers["numbers"].pop(0)


#############
#  answers  #
#############

def get_answer_1(numbers):
    time_start = time.perf_counter()
    invalid_number = get_invalid_number(numbers)
    time_spent = time.perf_counter() - time_start
    return {"value": invalid_number, "time": time_spent}


def get_answer_2(numbers):
    time_start = time.perf_counter()
    to_get = get_invalid_number(numbers)
    added_numbers = {"index": {"min": 0, "max": -1}, "numbers": [], "sum": 0, "value": {"min": float("inf"), "max": 0}}
    while added_numbers["sum"] != to_get:
        if added_numbers["sum"] < to_get:
            add_number(added_numbers, numbers)
        elif added_numbers["sum"] > to_get:
            remove_number(added_numbers, numbers)
    time_spent = time.perf_counter() - time_start
    return {"value": added_numbers["value"]["min"] + added_numbers["value"]["max"], "time": time_spent}


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
