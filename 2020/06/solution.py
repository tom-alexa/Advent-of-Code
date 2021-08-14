import time
from pathlib import PurePath

# --- Day 6: Custom Customs ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 6

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input")


###########
#  input  #
###########

def get_data_from_input():
    groups = []
    with open(INPUT_FILE, "r") as file:
        groups_dirty = file.read().split("\n\n")
        for group_dirty in groups_dirty:
            group = []
            group_modify = group_dirty.split("\n")
            for person in group_modify:
                if person:
                    group.append(person)
            groups.append(group)
    return groups


#############
#  answers  #
#############

def get_answer_1(groups):
    time_start = time.perf_counter()
    total_answers = {"answers": [], "count": 0}
    for group in groups:
        answers = set()
        for person in group:
            for answer in person:
                if answer not in answers:
                    answers.add(answer)
        total_answers["answers"].append(answers)
        total_answers["count"] += len(answers)
    time_spent = time.perf_counter() - time_start
    return {"value": total_answers["count"], "time": time_spent}


def get_answer_2(groups):
    time_start = time.perf_counter()
    common_answers = {"answers": [], "count": 0}
    for group in groups:
        first = True
        answers = set()
        for person in group:
            if first:
                for answer in person:
                    answers.add(answer)
            else:
                valid_answers = set()
                for answer in answers:
                    if answer in person:
                        valid_answers.add(answer)
                answers = valid_answers.copy()
            first = False
        common_answers["answers"].append(answers)
        common_answers["count"] += len(answers)
    time_spent = time.perf_counter() - time_start
    return {"value": common_answers["count"], "time": time_spent}


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
