import time
from pathlib import PurePath

# --- Day 3: Binary Diagnostic ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 3

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))


###############
#  functions  #
###############

def filtering(numbers, by_value):
    length = len(numbers[0])
    numbers = numbers.copy()
    for i in range(length):
        if len(numbers) == 1:
            break
        zeros = []
        ones = []
        for number in numbers:
            if number[i] == "0":
                zeros.append(number)
            else:
                ones.append(number)
        if by_value == "1":
            numbers = ones if len(ones) >= len(zeros) else zeros
        else:   # by_value == "0"
            numbers = ones if len(ones) < len(zeros) else zeros
    return int(numbers[0], 2)


#############
#  answers  #
#############

def get_answer_1(binary_numbers):
    time_start = time.perf_counter()

    counter = {i: 0 for i in range(len(binary_numbers[0]))}
    for number in binary_numbers:
        for i, char in enumerate(number):
            counter[i] += 1 if char == "1" else -1
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(binary_numbers[0])):
        gamma_rate += "1" if counter[i] >= 0 else "0"
        epsilon_rate += "0" if counter[i] >= 0 else "1"
    multiply = int(gamma_rate, 2) * int(epsilon_rate, 2)

    time_spent = time.perf_counter() - time_start
    return {"value": multiply, "time": time_spent}


def get_answer_2(binary_numbers):
    time_start = time.perf_counter()

    oxygen_generator_rating = filtering(binary_numbers, "1")
    co2_scrubber_rating = filtering(binary_numbers, "0")

    time_spent = time.perf_counter() - time_start
    return {"value": oxygen_generator_rating * co2_scrubber_rating, "time": time_spent}


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
