from functools import update_wrapper
import time
from pathlib import PurePath

# --- Day 19: Monster Messages ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 19

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        rules, messages = [x.split("\n") for x in file.read().split("\n\n")]
        rules_dict = {}
        for rule in rules:
            key, values_str = rule.split(": ")
            values = values_str.split(" | ")
            values_list = []
            for value in values:
                value_split = value.split(" ")
                value_list = []
                for specific_value in value_split:
                    if specific_value.isnumeric():
                        value_list.append(int(specific_value))
                    else:
                        value_list.append(specific_value.strip("\""))
                values_list.append(value_list)
            rules_dict[int(key)] = values_list
    return {"rules": rules_dict, "messages": messages}


###############
#  functions  #
###############

def check_sequence(rules, sequence, message):
    if not sequence:
        yield message
    else:
        index, *sequence = sequence
        for new_message in run(rules, index, message):
            yield from check_sequence(rules, sequence, new_message)


def expand(rules, sequences, message):
    for sequence in sequences:
        yield from check_sequence(rules, sequence, message)


def run(rules, index, message):
    if not isinstance(index, str):
        yield from expand(rules, rules[index], message)
    else:
        if message and message[0] == index:
            yield message[1:]


def match(rules, message):
    return any(m == "" for m in run(rules, 0, message))


def completely_match(rules_messages):
    total = 0
    for message in rules_messages["messages"]:
        if match(rules_messages["rules"], message):
            total += 1
    return total


#############
#  answers  #
#############

def get_answer_1(rules_messages):
    time_start = time.perf_counter()
    total = completely_match(rules_messages)
    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


def get_answer_2(rules_messages):
    time_start = time.perf_counter()
    r_a_m = rules_messages.copy()
    r_a_m["rules"] = {**r_a_m["rules"],
        8: [[42], [42, 8]],
        11: [[42, 31], [42, 11, 31]]
    }
    total = completely_match(r_a_m)
    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


###########
#  print  #
###########

def print_answers(answer_1, answer_2):
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"], 3)
    answer_2_time = round(answer_2["time"], 3)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    length_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    length_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indentation = " " * 2
    print(f"\n{indentation}{YEAR} > {DAY}")
    print(f"{indentation*2}Answer 1: {answer_1_value}{length_to_add_1} | {answer_1_time:.3f} s")
    print(f"{indentation*2}Answer 2: {answer_2_value}{length_to_add_2} | {answer_2_time:.3f} s\n")


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
