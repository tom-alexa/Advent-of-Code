import time
from pathlib import PurePath

# --- Day 18: Operation Order ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 18

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]


###############
#  functions  #
###############

def solve(status, char):
    if status["operator"][status["parentheses"]] == "*":
        solution = status["left"][status["parentheses"]] * int(char)
    elif status["operator"][status["parentheses"]] == "+":
        solution = status["left"][status["parentheses"]] + int(char)
    status["left"][status["parentheses"]] = solution


def solve_expression(expression_chars):
    status = {"parentheses": 0, "left": {}, "operator": {}}
    for char in expression_chars:
        if char.isnumeric():
            if not status["operator"].get(status["parentheses"]):
                status["left"][status["parentheses"]] = int(char)
            else:
                solve(status, char)
                status["operator"].pop(status["parentheses"])
        elif char in "()":
            if char == "(":
                status["parentheses"] += 1
            else:
                status["parentheses"] -= 1
                if not status["operator"].get(status["parentheses"]):
                    status["left"][status["parentheses"]] = status["left"][status["parentheses"]+1]
                else:
                    solve(status, status["left"][status["parentheses"]+1])
                    status["operator"].pop(status["parentheses"])
                status["left"].pop(status["parentheses"]+1)
        else:
            status["operator"][status["parentheses"]] = char
    return status["left"][0]


def add_parentheses(expression_chars):
    a = expression_chars[:]
    status = {"parentheses": 0, "plus": {}, "inserted": 0, "start_index": {}, "parentheses_indexes": {}}
    for i, char in enumerate(expression_chars[:]):
        if char.isnumeric():
            if status["plus"].get(status["parentheses"]):
                expression_chars.insert(i + status["inserted"] + 1, ")")
                expression_chars.insert(status["start_index"][status["parentheses"]], "(")
                status["inserted"] += 2
                status["plus"].pop(status["parentheses"])
            else:
                status["start_index"][status["parentheses"]] = i + status["inserted"]

        elif char in ("()"):
            if char == "(":
                if not status["plus"].get(status["parentheses"]):
                    status["start_index"][status["parentheses"]] = i + status["inserted"]
                status["parentheses"] += 1
                status["parentheses_indexes"][status["parentheses"]] = i + status["inserted"]

            else:
                status["parentheses"] -= 1
                if status["plus"].get(status["parentheses"]):
                    expression_chars.insert(i + status["inserted"], ")")
                    expression_chars.insert(status["start_index"][status["parentheses"]], "(")
                    status["inserted"] += 2
                    status["plus"].pop(status["parentheses"])
        else:
            if char == "+":
                status["plus"][status["parentheses"]] = True
    return expression_chars


#############
#  answers  #
#############

def get_answer_1(expressions):
    time_start = time.perf_counter()

    total = 0
    for expression in expressions:
        chars = [char for char in expression if char != " "]
        total += solve_expression(chars)

    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


def get_answer_2(expressions):
    time_start = time.perf_counter()

    total = 0
    for expression in expressions:
        chars = [char for char in expression if char != " "]
        expression = add_parentheses(chars[:])
        total += solve_expression(expression)

    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


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
