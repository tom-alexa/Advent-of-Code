import time
from pathlib import PurePath

# --- Day 8: Handheld Halting ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 8

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input")


###########
#  input  #
###########

def get_data_from_input():
    program = []
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            operation, argument = line.strip().split(" ")
            program.append({"operation": operation, "argument": int(argument)})
    return program


###############
#  functions  #
###############

def do_instructions(program, current_data):
    current_data["used"].add(current_data["index"])
    instruction = program[current_data["index"]]
    operation = instruction["operation"]
    argument = instruction["argument"]
    if operation == "acc":
        current_data["accumulator"] += argument
    elif operation == "jmp":
        current_data["index"] += argument
        return
    current_data["index"] += 1


#############
#  answers  #
#############

def get_answer_1(program):
    time_start = time.perf_counter()
    current_data = {"accumulator": 0, "index": 0, "used": set()}
    while True:
        if current_data["index"] in current_data["used"]:
            break
        do_instructions(program, current_data)
    time_spent = time.perf_counter() - time_start
    return {"value": current_data["accumulator"], "time": time_spent}


def get_answer_2(program):
    time_start = time.perf_counter()
    program_lenght = len(program)
    for instruction_to_change in program:
        if instruction_to_change["operation"] == "jmp":
            instruction_to_change["operation"] = "nop"
            changed = "jmp"
        elif instruction_to_change["operation"] == "nop":
            instruction_to_change["operation"] = "jmp"
            changed = "nop"
        else:
            continue

        current_data = {"accumulator": 0, "index": 0, "used": set()}
        infinite = True
        while True:
            if current_data["index"] >= program_lenght:
                infinite = False
                break
            if current_data["index"] in current_data["used"]:
                break
            do_instructions(program, current_data)

        if not infinite:
            break
        instruction_to_change["operation"] = changed

    time_spent = time.perf_counter() - time_start
    return {"value": current_data["accumulator"], "time": time_spent}


###########
#  print  #
###########

def print_answers(answer_1, answer_2):
    to_miliseconds = 1000
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"] * to_miliseconds, 3)
    answer_2_time = round(answer_2["time"] * to_miliseconds, 3)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    lenght_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    lenght_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indetation = " " * 2
    print(f"\n{indetation}{YEAR} > {DAY}")
    print(f"{indetation*2}Answer 1: {answer_1_value}{lenght_to_add_1} | {answer_1_time:.3f} ms")
    print(f"{indetation*2}Answer 2: {answer_2_value}{lenght_to_add_2} | {answer_2_time:.3f} ms\n")


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
