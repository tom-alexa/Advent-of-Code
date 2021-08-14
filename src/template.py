import time
from pathlib import PurePath

# ---  ---


###############
#  constants  #
###############

YEAR = 0
DAY = 0

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input")


###########
#  input  #
###########

def get_data_from_input():
    pass


###############
#  functions  #
###############


#############
#  answers  #
#############

def get_answer_1(puzzle_input):
    time_start = time.perf_counter()

    time_spent = time.perf_counter() - time_start
    return {"value": "", "time": time_spent}


def get_answer_2(puzzle_input):
    time_start = time.perf_counter()

    time_spent = time.perf_counter() - time_start
    return {"value": "", "time": time_spent}


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
