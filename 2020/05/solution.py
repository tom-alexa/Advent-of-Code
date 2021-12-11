import time
from pathlib import PurePath

# --- Day 5: Binary Boarding ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 5

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    binary_seats = set()
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            seat = line.strip()
            binary_seats.add(seat)
    return binary_seats


###############
#  functions  #
###############

def get_seats_and_max_min_id(binary_seats):
    seats = {}
    max_id = 0
    min_id = float("inf")
    for binary_seat in binary_seats:
        row = 0
        column = 0
        for i, letter in enumerate(binary_seat):
            if letter == "B":
                row += 2**(6 - i)
            elif letter == "R":
                column += 2**(2 - (i - 7))
        seat_id = (row * 8) + column
        seats[seat_id] = {"row": row, "column": column}
        if seat_id > max_id:
            max_id = seat_id
        elif seat_id < min_id:
            min_id = seat_id
    return {"seats": seats, "max_id": max_id, "min_id": min_id}


#############
#  answers  #
#############

def get_answer_1(binary_seats):
    time_start = time.perf_counter()
    max_id = get_seats_and_max_min_id(binary_seats)["max_id"]
    time_spent = time.perf_counter() - time_start
    return {"value": max_id, "time": time_spent}


def get_answer_2(binary_seats):
    time_start = time.perf_counter()
    database = get_seats_and_max_min_id(binary_seats)
    my_seat_id = None
    for seat_id in range(database["min_id"], database["max_id"] + 1):
        try:
            _ = database["seats"][seat_id]
        except KeyError:
            my_seat_id = seat_id
            break
    time_spent = time.perf_counter() - time_start
    return {"value": my_seat_id, "time": time_spent}


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
