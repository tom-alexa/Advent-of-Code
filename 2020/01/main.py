import time


# --- Day 1: Report Repair ---

SUM_TO_GET = 2020


def get_data_from_input():
    with open("2020/01/input", "r") as file:
        expense_report = set()
        for line in file.readlines():
            expense = int(line.strip())
            expense_report.add(expense)
    return expense_report


def get_answer_1(expense_report):
    time_start = time.perf_counter()
    values_to_get = set()
    for expense in expense_report:
        value_to_get = SUM_TO_GET - expense
        if expense in values_to_get:
            time_spent = time.perf_counter() - time_start
            return {"value": expense * value_to_get, "time": time_spent}
        values_to_get.add(value_to_get)


def get_answer_2(expense_report):
    time_start = time.perf_counter()
    for m in expense_report:
        for n in expense_report:
            for o in expense_report:
                if m+n+o == SUM_TO_GET:
                    time_spent = time.perf_counter() - time_start
                    return {"value": m*n*o, "time": time_spent}


def print_answers(answer_1, answer_2):
    to_miliseconds = 1000
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"] * to_miliseconds, 5)
    answer_2_time = round(answer_2["time"] * to_miliseconds, 5)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    lenght_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    lenght_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indetation = " " * 2
    print(f"\n{indetation}2020 > 01")
    print(f"{indetation*2}Answer 1: {answer_1_value}{lenght_to_add_1} | {answer_1_time} ms")
    print(f"{indetation*2}Answer 2: {answer_2_value}{lenght_to_add_2} | {answer_2_time} ms\n")


def main():
    expense_report = get_data_from_input()
    answer_1 = get_answer_1(expense_report)
    answer_2 = get_answer_2(expense_report)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
