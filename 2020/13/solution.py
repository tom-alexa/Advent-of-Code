import time
from pathlib import PurePath

# --- Day 13: Shuttle Search ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 13

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")

START_BUS_TIMESTAMP = 0


###########
#  input  #
###########

def parse_input():
    schedules = {}
    with open(INPUT_FILE, "r") as file:
        for i, line in enumerate(file.readlines()):
            if i == 0:
                schedules["timestamp"] = int(line.strip())
            elif i == 1:
                schedules["ids"] = [ int(bus_id) if bus_id != "x" else bus_id for bus_id in line.strip().split(",") ]
    return schedules


###############
#  functions  #
###############

def mod_inverse(a, m):
    """
    Find some x such that (a*x) % m == 1
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


#############
#  answers  #
#############

def get_answer_1(schedules):
    time_start = time.perf_counter()
    bus_wait = {}
    earliest_timestamp = {"id": None, "time": float("inf")}

    for bus_id in schedules["ids"]:
        if bus_id == "x":
            continue
        bus_wait[bus_id] = START_BUS_TIMESTAMP + bus_id - (schedules["timestamp"] % bus_id)
        if bus_wait[bus_id] < earliest_timestamp["time"]:
            earliest_timestamp["id"] = bus_id
            earliest_timestamp["time"] = bus_wait[bus_id]

    time_spent = time.perf_counter() - time_start
    return {"value": earliest_timestamp["id"] * earliest_timestamp["time"], "time": time_spent}


def get_answer_2(schedules):
    """
    Chinese remainder theorem
    """
    time_start = time.perf_counter()
    differences = []
    full = 1

    for i, bus_id in enumerate(schedules["ids"]):
        if bus_id == "x":
            continue
        difference = i % bus_id
        differences.append({"id": bus_id, "difference": (bus_id - difference) % bus_id, "i": i})
        full *= bus_id

    total = 0
    for bus in differences:
        bus_id = bus["id"]
        difference = bus["difference"]
        part = full // bus_id
        inverse = mod_inverse(part, bus_id)
        total += (inverse * part * difference)

    time_spent = time.perf_counter() - time_start
    return {"value": total % full, "time": time_spent}


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
