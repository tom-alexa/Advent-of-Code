import time
from pathlib import PurePath

# --- Day 1: Sonar Sweep ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 1

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        depth = list(map(lambda x: int(x.strip()), file.readlines()))
    return depth


#############
#  answers  #
#############

def get_answer_1(depth):
    time_start = time.perf_counter()

    increased = -1
    previous = 0
    for d in depth:
        if d > previous:
            increased += 1
        previous = d

    time_spent = time.perf_counter() - time_start
    return {"value": increased, "time": time_spent}


def get_answer_2(depth):
    time_start = time.perf_counter()

    total_sum = depth[0] + depth[1] + depth[2]
    min_index = 0
    max_index = 2
    increased = 0
    for _ in range(len(depth) - 3):
        current_sum = total_sum - depth[min_index] + depth[max_index + 1]
        if current_sum > total_sum:
            increased += 1
        total_sum = current_sum
        min_index += 1
        max_index += 1

    time_spent = time.perf_counter() - time_start
    return {"value": increased, "time": time_spent}


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
