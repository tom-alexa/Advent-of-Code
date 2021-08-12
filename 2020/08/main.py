from sys import int_info
import time

# --- Day 8: Handheld Halting ---


def get_data_from_input():
    program = []
    with open("2020/08/input", "r") as file:
        for line in file.readlines():
            operation, argument = line.strip().split(" ")
            program.append({"operation": operation, "argument": int(argument)})
    return program


def get_answer_1(program):
    time_start = time.perf_counter()
    used_instructions = set()
    accumulator = 0
    index = 0
    while True:
        if index in used_instructions:
            break

        instruction = program[index]
        operation = instruction["operation"]
        argument = instruction["argument"]

        if operation == "acc":
            accumulator += argument
        elif operation == "jmp":
            index += argument
            continue

        used_instructions.add(index)
        index += 1

    time_spent = time.perf_counter() - time_start
    return {"value": accumulator, "time": time_spent}


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

        used_instructions = set()
        accumulator = 0
        index = 0
        infinite = True
        while True:
            if index >= program_lenght:
                infinite = False
                break
            if index in used_instructions:
                break

            used_instructions.add(index)
            instruction = program[index]
            operation = instruction["operation"]
            argument = instruction["argument"]
            if operation == "acc":
                accumulator += argument
            elif operation == "jmp":
                index += argument
                continue
            index += 1

        if not infinite:
            break
        instruction_to_change["operation"] = changed

    time_spent = time.perf_counter() - time_start
    return {"value": accumulator, "time": time_spent}


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
    print(f"\n{indetation}2020 > 08")
    print(f"{indetation*2}Answer 1: {answer_1_value}{lenght_to_add_1} | {answer_1_time:.3f} ms")
    print(f"{indetation*2}Answer 2: {answer_2_value}{lenght_to_add_2} | {answer_2_time:.3f} ms\n")


def main():
    puzzle_input = get_data_from_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
