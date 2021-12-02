import time
from pathlib import PurePath

# --- Day 12: Rain Risk ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 12

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")

START_POS = (0, 0)
WAYPOINT_START = (10, -1)


###########
#  input  #
###########

def get_data_from_input():
    instructions = []
    with open(INPUT_FILE, "r") as file:
        for line in file.readlines():
            instruction = {"action": line[0], "value": int(line[1:].strip())}
            instructions.append(instruction)
    return instructions


###############
#  functions  #
###############

def update_position_1(position, instruction):
    action = instruction["action"]
    value = instruction["value"]
    direction = position["direction"]
    if action == "N":
        position["y"] -= value
    elif action == "S":
        position["y"] += value
    elif action == "E":
        position["x"] += value
    elif action == "W":
        position["x"] -= value
    elif action == "L":
        position["direction"] = (360 + direction - value) % 360
    elif action == "R":
        position["direction"] = (direction + value) % 360
    elif action == "F":
        if direction == 0:
            position["y"] -= value
        elif direction == 90:
            position["x"] += value
        elif direction == 180:
            position["y"] += value
        elif direction == 270:
            position["x"] -= value


def update_position_2(position, instruction):
    action = instruction["action"]
    value = instruction["value"]
    waypoint_x = position["waypoint"]["x"]
    waypoint_y = position["waypoint"]["y"]
    if action == "N":
        position["waypoint"]["y"] -= value
    elif action == "S":
        position["waypoint"]["y"] += value
    elif action == "E":
        position["waypoint"]["x"] += value
    elif action == "W":
        position["waypoint"]["x"] -= value
    elif action == "L" or action == "R":
        if action == "L":
            value = 360 - value
        if value == 90:
            position["waypoint"]["x"] = -waypoint_y
            position["waypoint"]["y"] = waypoint_x
        elif value == 180:
            position["waypoint"]["x"] = -waypoint_x
            position["waypoint"]["y"] = -waypoint_y
        elif value == 270:
            position["waypoint"]["x"] = waypoint_y
            position["waypoint"]["y"] = -waypoint_x
    elif action == "F":
        position["x"] += waypoint_x * value
        position["y"] += waypoint_y * value


#############
#  answers  #
#############

def get_answer_1(instructions):
    time_start = time.perf_counter()
    position = {"direction": 90, "x": START_POS[0], "y": START_POS[1]}
    for instruction in instructions:
        update_position_1(position, instruction)
    time_spent = time.perf_counter() - time_start
    return {"value": abs(position["x"]) + abs(position["y"]), "time": time_spent}


def get_answer_2(instructions):
    time_start = time.perf_counter()
    position = {"x": START_POS[0], "y": START_POS[1], "waypoint": {"x": WAYPOINT_START[0], "y": WAYPOINT_START[1]}}
    for instruction in instructions:
        update_position_2(position, instruction)
    time_spent = time.perf_counter() - time_start
    return {"value": abs(position["x"] + abs(position["y"])), "time": time_spent}


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
