import time

# --- Day 9: Encoding Error ---

PREAMBLE_LENGHT = 25


###########
#  input  #
###########

def get_data_from_input():
    numbers = []
    with open("2020/09/input", "r") as file:
        for line in file.readlines():
            number = int(line.strip())
            numbers.append(number)
    return numbers


###############
#  functions  #
###############

def is_valid(number, preamble):
    for first_preamble_number in preamble:
        for second_preamble_number in preamble:
            if number == first_preamble_number + second_preamble_number:
                return True
    return False


def get_invalid_number(numbers):
    preamble = numbers[:PREAMBLE_LENGHT]
    for number in numbers[PREAMBLE_LENGHT:]:
        if not is_valid(number, preamble):
            return number
        preamble = preamble[1:]
        preamble.append(number)


def add_number(added_numbers, numbers):
    added_numbers["index"]["max"] += 1
    added_numbers["numbers"].append(numbers[added_numbers["index"]["max"]])
    added_numbers["sum"] += numbers[added_numbers["index"]["max"]]


def remove_number(added_numbers, numbers):
    added_numbers["sum"] -= numbers[added_numbers["index"]["min"]]
    added_numbers["index"]["min"] += 1
    added_numbers["numbers"].pop(0)


#############
#  answers  #
#############

def get_answer_1(numbers):
    time_start = time.perf_counter()
    invalid_number = get_invalid_number(numbers)
    time_spent = time.perf_counter() - time_start
    return {"value": invalid_number, "time": time_spent}


def get_answer_2(numbers):
    time_start = time.perf_counter()
    to_get = get_invalid_number(numbers)
    added_numbers = {"index": {"min": 0, "max": -1}, "numbers": [], "sum": 0}
    while added_numbers["sum"] != to_get:
        if added_numbers["sum"] < to_get:
            add_number(added_numbers, numbers)
        elif added_numbers["sum"] > to_get:
            remove_number(added_numbers, numbers)
    time_spent = time.perf_counter() - time_start
    return {"value": min(added_numbers["numbers"]) + max(added_numbers["numbers"]), "time": time_spent}


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
    print(f"\n{indetation}2020 > 09")
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
