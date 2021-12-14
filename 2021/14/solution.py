import time
from pathlib import PurePath

# --- Day 14: Extended Polymerization ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 14

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    with open(INPUT_FILE, "r") as file:
        template, pairs = file.read().split("\n\n")
        pair_insertion = {}
        for pair in pairs.split("\n"):
            insertion_pair, insertion_letter = pair.split(" -> ")
            pair_insertion[insertion_pair] = insertion_letter
    return {"template": list(template), "insertion": pair_insertion}


###############
#  functions  #
###############

def create_template_pairs(template):
    template_pairs = {}
    for i in range(len(template) - 1):
        template_pairs[f"{template[i]}{template[i + 1]}"] = template_pairs.get(f"{template[i]}{template[i + 1]}", 0) + 1
    return template_pairs


def step(template_pairs, insertion):
    new_template_pairs = {}
    for pair in template_pairs:
        first_new = f'{pair[0]}{insertion[pair]}'
        second_new = f'{insertion[pair]}{pair[1]}'
        new_template_pairs[first_new] = template_pairs[pair] + new_template_pairs.get(first_new, 0)
        new_template_pairs[second_new] = template_pairs[pair] + new_template_pairs.get(second_new, 0)
    return new_template_pairs


def counter(template_pair):
    count = {}
    for i, (pair, pair_count) in enumerate(template_pair.items()):
        count[pair[1]] = count.get(pair[1], 0) + pair_count
        if i == 0:
            count[pair[0]] = count.get(pair[0], 0) + pair_count
    return max(count.values()), min(count.values())


#############
#  answers  #
#############

def get_answer_1(template_insertion):
    time_start = time.perf_counter()

    template_pairs = create_template_pairs(template_insertion["template"].copy())
    for _ in range(10):
        template_pairs = step(template_pairs, template_insertion["insertion"])
    count_max, count_min = counter(template_pairs)

    time_spent = time.perf_counter() - time_start
    return {"value": count_max - count_min, "time": time_spent}


def get_answer_2(template_insertion):
    time_start = time.perf_counter()

    template_pairs = create_template_pairs(template_insertion["template"].copy())
    for _ in range(40):
        template_pairs = step(template_pairs, template_insertion["insertion"])
    count_max, count_min = counter(template_pairs)

    time_spent = time.perf_counter() - time_start
    return {"value": count_max - count_min, "time": time_spent}


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
