import time
from pathlib import PurePath

# --- Day 16: Ticket Translation ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 16

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        after_split = file.read().split("\n\n")
        fields = {"names": {}, "my_ticket": [], "nearby_tickets": []}
        for line in after_split[0].split("\n"):
            name, values =  line.split(": ")
            values_1, values_2 = values.split(" or ")
            minimum_1, maximum_1 = tuple(map(int, values_1.split("-")))
            minimum_2, maximum_2 = tuple(map(int, values_2.split("-")))
            fields["names"][name] = [
                {"max": maximum_1, "min": minimum_1},
                {"max": maximum_2, "min": minimum_2}
            ]
        fields["my_ticket"] = list(map(int, after_split[1].split("\n")[1].split(",")))
        for line in after_split[2].split("\n")[1:]:
            fields["nearby_tickets"].append(list(map(int, line.split(","))))
    return fields


###############
#  functions  #
###############

def mapper(arrays):
    min_max = []
    for conditions in arrays.values():
        for condition in conditions:
            if not min_max:
                min_max.append([condition["min"], condition["max"]])
                continue
            for i, limit in enumerate(min_max[:]):
                if condition["min"] < limit[0]:
                    min_max.insert(i, [condition["min"], max(condition["max"], limit[1])])
                    added = 1
                    while (i + added) < len(min_max):
                        if condition["max"] <= min_max[i + 1][0]:
                            break
                        if condition["max"] < min_max[i + 1][1]:
                            min_max[i][1] = min_max[i + 1][1]
                            del min_max[i + 1]
                            break
                        del min_max[i + added]
                        added -= 1
                    break
            else:
                min_max.append([condition["min"], condition["max"]])
                if condition["max"] < min_max[-2][1]:
                    del min_max[-1]
                elif condition["min"] + 1 <= min_max[-2][1]:
                    min_max[-1][0] = min_max[-2][0]
                    del min_max[-2]
    return min_max


def get_valid_tickets(tickets, limits):
    valid_tickets = []
    for ticket in tickets:
        valid = True
        for value in ticket:
            for limit in limits:
                if (value >= limit[0]) and (value <= limit[1]):
                    break
            else:
                valid = False
        if valid: valid_tickets.append(ticket)
    return valid_tickets


#############
#  answers  #
#############

def get_answer_1(fields):
    time_start = time.perf_counter()

    limits = mapper(fields["names"])
    error_rate = 0
    for ticket in fields["nearby_tickets"]:
        for value in ticket:
            for limit in limits:
                if (value >= limit[0]) and (value <= limit[1]):
                    break
            else:
                error_rate += value

    time_spent =  time.perf_counter() - time_start
    return {"value": error_rate, "time": time_spent}


def get_answer_2(fields):
    time_start = time.perf_counter()

    limits = mapper(fields["names"])
    valid_tickets = get_valid_tickets(fields["nearby_tickets"], limits)
    valid_field_indexes = {}
    for field, values in fields["names"].items():
        valid_field_indexes[field] = {index for index in range(len(fields["my_ticket"]))}
        for ticket in valid_tickets + [fields["my_ticket"]]:
            for i, ticket_value in enumerate(ticket):
                if i not in valid_field_indexes[field]:
                    continue
                if not ((ticket_value >= values[0]["min"] and ticket_value <= values[0]["max"]) or (ticket_value >= values[1]["min"] and ticket_value <= values[1]["max"])):
                    valid_field_indexes[field].remove(i)
    indexes = {}
    for index in range(len(fields["my_ticket"])):
        indexes[index] = set()
        for field, valid_indexes in valid_field_indexes.items():
            if index in valid_indexes:
                indexes[index].add(field)

    added = set()
    while True:
        find_index = None
        for index, values in indexes.items():
            if index in added:
                continue
            if len(values) == 1:
                find_index = index
                to_connect = list(values)[0]
                break
        for index in indexes:
            if index != find_index:
                indexes[index].discard(to_connect)
        added.add(find_index)
        if len(added) == len(fields["my_ticket"]):
            break

    multiply = 1
    for index, field in indexes.items():
        field = list(field)[0]
        if "departure" in field:
            multiply *= fields["my_ticket"][index]

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
    puzzle_input = get_data_from_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
