import time
from pathlib import PurePath

# --- Day 1: Report Repair ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 1

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")

SUM_TO_GET = 2020


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        expense_report = set()
        for line in file.readlines():
            expense = int(line.strip())
            expense_report.add(expense)
    return expense_report


#############
#  answers  #
#############

def get_answer_1(expense_report):
    time_start = time.perf_counter()
    values_to_get = set()
    for expense in expense_report:
        to_get = SUM_TO_GET - expense
        if expense in values_to_get:
            time_spent = time.perf_counter() - time_start
            return {"value": expense * to_get, "time": time_spent}
        values_to_get.add(to_get)


def get_answer_2(expense_report):
    time_start = time.perf_counter()
    used_expenses = set()
    values_to_get = {}
    for expense in expense_report:
        if expense in values_to_get:
            value_1, value_2 = values_to_get[expense]
            time_spent = time.perf_counter() - time_start
            return {"value": expense * value_1 * value_2, "time": time_spent}
        for used_expense in used_expenses:
            to_get = SUM_TO_GET - expense - used_expense
            values_to_get[to_get] = {expense, used_expense}
        used_expenses.add(expense)


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
