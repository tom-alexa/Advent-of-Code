import time
from pathlib import PurePath

# --- Day 13: Transparent Origami ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 13

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        instructions = {"dots": [], "folds": []}
        dots, folds = map(lambda x: x.split("\n"), file.read().split("\n\n"))
        for dot in dots:
            x, y = map(int, dot.split(","))
            instructions["dots"].append((x, y))
        for fold in folds:
            important = fold.split(" ")[2]
            x_or_y, number = important.split("=")
            instructions["folds"].append((x_or_y, int(number)))
    return instructions


###############
#  functions  #
###############

def fold_transparent(dots, folds, fold_index):
    new_dots = []
    direction = folds[fold_index][0]
    fold_line = folds[fold_index][1]
    for i, instruction in enumerate(dots):
        new_index = 0 if direction == "x" else 1
        same_index = 0 if direction == "y" else 1
        new_dots.append([instruction[same_index]])
        if instruction[new_index] > fold_line:
            new_dots[i].insert(new_index, fold_line - (instruction[new_index] - fold_line))
        else:
            new_dots[i].insert(new_index, instruction[new_index])
    set_dots = set()
    for dot in new_dots:
        set_dots.add(tuple(dot))
    return list(set_dots)


#############
#  answers  #
#############

def get_answer_1(instructions):
    time_start = time.perf_counter()
    dots = fold_transparent(instructions["dots"].copy(), instructions["folds"], 0)
    time_spent = time.perf_counter() - time_start
    return {"value": len(dots), "time": time_spent}


def get_answer_2(instructions):
    time_start = time.perf_counter()
    dots = instructions["dots"].copy()
    for fold_index in range(len(instructions["folds"])):
        dots = fold_transparent(dots, instructions["folds"], fold_index)
    max_x = max(dots, key=lambda x: x[0])[0]
    max_y = max(dots, key=lambda x: x[1])[1]
    spaces = " " * 6
    to_print = ""
    for y in range(max_y + 1):
        to_print += f"\n{spaces}"
        for x in range(max_x + 1):
            if (x, y) in dots:
                to_print += "█"
            else:
                to_print += " "
    time_spent = time.perf_counter() - time_start
    return {"value": to_print, "time": time_spent}


###########
#  print  #
###########

def print_answers(answer_1, answer_2):
    to_milliseconds = 1000
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"] * to_milliseconds, 3)
    answer_2_time = round(answer_2["time"] * to_milliseconds, 3)

    to_add = "↓" * len(str(answer_1_value))

    indentation = " " * 2
    print(f"\n{indentation}{YEAR} > {DAY}")
    print(f"{indentation*2}Answer 1: {answer_1_value} | {answer_1_time:.3f} ms")
    print(f"{indentation*2}Answer 2: {to_add} | {answer_2_time:.3f} ms\n{answer_2_value}\n")


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
