import time
from pathlib import PurePath

# --- Day 9: Smoke Basin ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 9

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        return [x.strip() for x in file.readlines()]


###############
#  functions  #
###############

def check_up(row, column, places, low_point=True):
    if low_point:
        if row <= 0 or (int(places[row][column]) < int(places[row - 1][column])):
            return True
    else:
        if row > 0 and (int(places[row][column]) < int(places[row - 1][column])):
            return True
    return False


def check_down(row, column, places, low_point=True):
    if low_point:
        if (row >= len(places) - 1) or (int(places[row][column]) < int(places[row + 1][column])):
            return True
    else:
        if (row < len(places) - 1) and (int(places[row][column]) < int(places[row + 1][column])):
            return True
    return False


def check_left(row, column, places, low_point=True):
    if low_point:
        if column <= 0 or (int(places[row][column]) < int(places[row][column - 1])):
            return True
    else:
        if column > 0 and (int(places[row][column]) < int(places[row][column - 1])):
            return True
    return False


def check_right(row, column, places, low_point=True):
    if low_point:
        if (column >= len(places[row]) - 1) or (int(places[row][column]) < int(places[row][column + 1])):
            return True
    else:
        if (column < len(places[row]) - 1) and (int(places[row][column]) < int(places[row][column + 1])):
            return True
    return False


def bigger(biggest, number):
    biggest.append(number)
    if len(biggest) <= 3:
        return biggest
    minimum = min(biggest + [number])
    biggest.remove(minimum)
    return biggest

#############
#  answers  #
#############

def get_answer_1(places):
    time_start = time.perf_counter()

    risk_sum = 0
    for row in range(len(places)):
        for column in range(len(places[0])):
            if check_up(row, column, places) and check_down(row, column, places) and check_left(row, column, places) and check_right(row, column, places):
                risk_sum += int(places[row][column]) + 1

    time_spent = time.perf_counter() - time_start
    return {"value": risk_sum, "time": time_spent}


def get_answer_2(places):
    time_start = time.perf_counter()

    biggest = []
    for row in range(len(places)):
        for column in range(len(places[0])):
            if check_up(row, column, places) and check_down(row, column, places) and check_left(row, column, places) and check_right(row, column, places):
                basin = {(row, column)}
                to_check = {(row, column)}
                while to_check:
                    x, y = to_check.pop()
                    if check_up(x, y, places, low_point=False):
                        if int(places[x - 1][y]) < 9 and (x - 1, y) not in basin:
                            to_check.add((x - 1, y))
                            basin.add((x - 1, y))
                    if check_down(x, y, places, low_point=False):
                        if int(places[x + 1][y]) < 9 and (x + 1, y) not in basin:
                            to_check.add((x + 1, y))
                            basin.add((x + 1, y))
                    if check_left(x, y, places, low_point=False):
                        if int(places[x][y - 1]) < 9 and (x, y - 1) not in basin:
                            to_check.add((x, y - 1))
                            basin.add((x, y - 1))
                    if check_right(x, y, places, low_point=False):
                        if int(places[x][y + 1]) < 9 and (x, y + 1) not in basin:
                            to_check.add((x, y + 1))
                            basin.add((x, y + 1))
                biggest = bigger(biggest, len(basin))

    multiply = 1
    for number in biggest:
        multiply *= number

    time_spent = time.perf_counter() - time_start
    return {"value": multiply, "time": time_spent}


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
