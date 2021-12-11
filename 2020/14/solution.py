import time
from pathlib import PurePath

# --- Day 14: Docking Data ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 14

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    programs = []
    program = {}
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            data = line.strip().split(" = ")
            if data[0] == "mask":
                if program:
                    programs.append(program)
                    program = {}
                program["mask"] = data[1]
                program["memory"] = []
                continue
            program["memory"].append({"address": data[0][4:-1], "value": data[1]})
    programs.append(program)
    return programs


###############
#  functions  #
###############

def get_new_value(value, mask):
    new_value = ""
    old_value = "0" * (len(mask) - len(bin(int(value)))) + bin(int(value))
    for i in range(len(mask)):
        if mask[i] != "X":
            new_value += mask[i]
            continue
        new_value += old_value[i]
    return new_value


def get_decimal(binary_number):
    number = 0
    for i in range(len(binary_number)):
        number += 2**(len(binary_number) - 1 - i) if binary_number[i] == "1" else 0
    return number


def all_addresses(old_address: int, mask):
    address = old_address | int(mask.replace("X", "0"), 2)
    positions = [35 - i for i, char in enumerate(mask) if char == "X"]
    return addresses_from_position_indexes(address, positions)


def addresses_from_position_indexes(address, positions):
    if len(positions) == 1:
        return [address | (1 << positions[0]), address & ~(1 << positions[0])]
    return addresses_from_position_indexes(address | (1 << positions[0]), positions[1:]) + \
        addresses_from_position_indexes(address & ~(1 << positions[0]), positions[1:])


#############
#  answers  #
#############

def get_answer_1(programs):
    time_start = time.perf_counter()

    memory = {}
    for program in programs:
        mask = program["mask"]
        for event in program["memory"]:
            address = event["address"]
            value = event["value"]
            memory[address] = get_new_value(value, mask)

    total = 0
    for value in memory.values():
        total += get_decimal(value)

    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


def get_answer_2(programs):
    time_start = time.perf_counter()

    memory = {}
    for program in programs:
        mask = program["mask"]
        for event in program["memory"]:
            old_address = event["address"]
            value = event["value"]
            addresses = all_addresses(int(old_address), mask)
            for address in addresses:
                memory[address] = value

    time_spent = time.perf_counter() - time_start
    return {"value": sum(map(int, memory.values())), "time": time_spent}


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
