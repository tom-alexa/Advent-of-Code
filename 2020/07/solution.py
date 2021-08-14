import time
from pathlib import PurePath

# --- Day 7: Handy Haversacks ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 7

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input")

MY_BAG = "shiny gold bag"


###########
#  input  #
###########

def get_data_from_input():
    bags_in = {}
    bags_out = {}
    used_bags = set()
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            line = line.strip().strip(".")
            bag_name_plural, contents = line.split(" contain ")
            bag_name = bag_name_plural[:-1]
            contents_bags = contents.split(", ")
            bags_in[bag_name] = []
            for contents_bag in contents_bags:
                if contents_bag != "no other bags":
                    string_to_number = ""
                    contents_bag_name_plural = ""
                    faze = 1
                    for letter in contents_bag:
                        if letter == " " and faze == 1:
                            faze = 2
                            continue
                        if faze == 1:
                            string_to_number += letter
                        elif faze == 2:
                            contents_bag_name_plural += letter
                    number_of_bags = int(string_to_number)
                    contents_bag_name = contents_bag_name_plural if contents_bag_name_plural[-1] != "s" else contents_bag_name_plural[:-1]
                    bags_in[bag_name].append({"name": contents_bag_name, "total": number_of_bags})
                    if contents_bag_name not in used_bags:
                        bags_out[contents_bag_name] = set()
                        used_bags.add(contents_bag_name)
                    bags_out[contents_bag_name].add(bag_name)
    for bag in bags_in:
        if bag not in bags_out:
            bags_out[bag] = set()
    return {"in": bags_in, "out": bags_out}


###############
#  functions  #
###############

def get_bigger_bags(bag_name, bags_out, bigger_bags):
    for bigger_bag in bags_out[bag_name]:
        bigger_bags.add(bigger_bag)
        get_bigger_bags(bigger_bag, bags_out, bigger_bags)
    return bigger_bags


def get_smaller_bags(bag_name, bags_in, smaller_bags):
    for smaller_bag in bags_in[bag_name]:
        smaller_bags["bags"].append(smaller_bag)
        smaller_bags["total"] += smaller_bag["total"]
        for _ in range(smaller_bag["total"]):
            get_smaller_bags(smaller_bag["name"], bags_in, smaller_bags)
    return smaller_bags


#############
#  answers  #
#############

def get_answer_1(bags):
    time_start = time.perf_counter()
    bigger_bags = get_bigger_bags(MY_BAG, bags["out"], set())
    time_spent = time.perf_counter() - time_start
    return {"value": len(bigger_bags), "time": time_spent}


def get_answer_2(bags):
    time_start = time.perf_counter()
    smaller_bags = get_smaller_bags(MY_BAG, bags["in"], {"bags": [], "total": 0})
    time_spent = time.perf_counter() - time_start
    return {"value": smaller_bags["total"], "time": time_spent}


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
