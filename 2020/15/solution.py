import time
from pathlib import PurePath

# --- Day 15: Rambunctious Recitation ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 15

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        return list(map(lambda x: int(x.strip()), file.read().split(",")))


###############
#  functions  #
###############

def play(starting_numbers, turns):
    if turns > 10000000:
        print()
        indentation = " " * 6

    last_indexes = {}
    for i, number in enumerate(starting_numbers):
        if (i + 1) != len(starting_numbers):
            last_indexes[number] = i + 1
        last_number = number

    for i in range(len(starting_numbers) + 1, turns + 1):
        new = 0 if last_indexes.get(last_number) == None else (i - last_indexes[last_number] - 1)
        last_indexes[last_number] = i - 1
        last_number = new
        if (turns > 1000000) and (i % 1000000 == 0):
            print(f"{indentation}{i//1000000}/{int(turns/1000000)}")
    return new


#############
#  answers  #
#############

def get_answer_1(numbers):
    time_start = time.perf_counter()
    number = play(numbers, 2020)
    time_spent = time.perf_counter() - time_start
    return {"value": number, "time": time_spent}


def get_answer_2(numbers):
    time_start = time.perf_counter()
    number = play(numbers, 30000000)
    time_spent = time.perf_counter() - time_start
    return {"value": number, "time": time_spent}


###########
#  print  #
###########

def print_answers(answer_1, answer_2):
    to_milliseconds = 1000
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"] * to_milliseconds, 3)
    answer_2_time = round(answer_2["time"], 3)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    length_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    length_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indentation = " " * 2
    print(f"\n{indentation}{YEAR} > {DAY}")
    print(f"{indentation*2}Answer 1: {answer_1_value}{length_to_add_1} | {answer_1_time:.3f} ms")
    print(f"{indentation*2}Answer 2: {answer_2_value}{length_to_add_2} | {answer_2_time:.3f} s\n")


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
