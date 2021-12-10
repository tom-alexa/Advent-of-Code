import time
from pathlib import PurePath

# --- Day 10: Syntax Scoring ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 10

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        return [x.strip() for x in file.readlines()]


#############
#  answers  #
#############

def get_answer_1(lines):
    time_start = time.perf_counter()

    score = {"total": 0, ")": 3, "]": 57, "}": 1197, ">": 25137}
    reverse_char = {")": "(", "]": "[", "}": "{", ">": "<"}
    for line in lines:
        opens = ""
        for char in line:
            if char in ["(", "[", "{", "<"]:
                opens += char
                continue
            if not opens or reverse_char[char] != opens[-1]:
                score["total"] += score[char]
                break
            opens = opens[:-1]

    time_spent = time.perf_counter() - time_start
    return {"value": score["total"], "time": time_spent}


def get_answer_2(lines):
    time_start = time.perf_counter()

    score = {"(": 1, "[": 2, "{": 3, "<": 4}
    incompletes = []
    reverse_char = {")": "(", "]": "[", "}": "{", ">": "<"}
    for line in lines:
        opens = ""
        valid = True
        for char in line:
            if char in ["(", "[", "{", "<"]:
                opens += char
                continue
            if not opens or reverse_char[char] != opens[-1]:
                valid = False
                break
            opens = opens[:-1]
        if not (opens and valid):
            continue
        total = 0
        for char in opens[::-1]:
            total *= 5
            total += score[char]
        incompletes.append(total)
    middle = sorted(incompletes)[len(incompletes)//2]

    time_spent = time.perf_counter() - time_start
    return {"value": middle, "time": time_spent}


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
