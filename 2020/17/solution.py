import time
from pathlib import PurePath

# --- Day 17: Conway Cubes ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 17

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    pocket_dimension = {}
    with open(INPUT_FILE, "r") as file:
        for i, line in enumerate(file.readlines()):
            for j, char in enumerate(line.strip()):
                pocket_dimension[(j, i, 0, 0)] = char
    return pocket_dimension


###############
#  functions  #
###############

def do_cycle(pocket_dimension, total_dimension=3):
    min_max = find_min_max(pocket_dimension)
    new_pocket_dimension = {}
    for x in range(min_max["x"][0], min_max["x"][1] + 1):
        for y in range(min_max["y"][0], min_max["y"][1] + 1):
            for z in range(min_max["z"][0], min_max["z"][1] + 1):
                if total_dimension < 4:
                    w_range = [0]
                else:
                    w_range = range(min_max["w"][0], min_max["w"][1] + 1)
                for w in w_range:
                    active_neighbours = count_neighbours(x, y, z, w, pocket_dimension, min_max, total_dimension=total_dimension)
                    if is_active(x, y, z, w, pocket_dimension, min_max):
                        if active_neighbours in [2, 3]:
                            new_pocket_dimension[(x, y, z, w)] = "#"
                        else:
                            new_pocket_dimension[(x, y, z, w)] = "."
                    else:
                        if active_neighbours == 3:
                            new_pocket_dimension[(x, y, z, w)] = "#"
                        else:
                            new_pocket_dimension[(x, y, z, w)] = "."
    return new_pocket_dimension


def find_min_max(pocket_dimension):
    min_max = {"x": [0, 0], "y": [0, 0], "z": [0, 0], "w": [0, 0]}
    for dimension in pocket_dimension:
        if dimension[0] < min_max["x"][0]:
            min_max["x"][0] = dimension[0]
        elif dimension[0] > min_max["x"][1]:
            min_max["x"][1] = dimension[0]
        if dimension[1] < min_max["y"][0]:
            min_max["y"][0] = dimension[1]
        elif dimension[1] > min_max["y"][1]:
            min_max["y"][1] = dimension[1]
        if dimension[2] < min_max["z"][0]:
            min_max["z"][0] = dimension[2]
        elif dimension[2] > min_max["z"][1]:
            min_max["z"][1] = dimension[2]
        if dimension[3] < min_max["w"][0]:
            min_max["w"][0] = dimension[3]
        elif dimension[3] > min_max["w"][1]:
            min_max["w"][1] = dimension[3]
    min_max["x"] = min_max["x"][0] - 1, min_max["x"][1] + 1
    min_max["y"] = min_max["y"][0] - 1, min_max["y"][1] + 1
    min_max["z"] = min_max["z"][0] - 1, min_max["z"][1] + 1
    min_max["w"] = min_max["w"][0] - 1, min_max["w"][1] + 1
    return min_max


def count_neighbours(x, y, z, w, pocket_dimension, min_max, total_dimension=3):
    count = 0
    for n_x in range(x - 1, x + 2):
        for n_y in range(y - 1, y + 2):
            for n_z in range(z - 1, z + 2):
                for n_w in range(w - 1, w + 2):
                    if total_dimension < 4 and n_w != w:
                        continue
                    if (n_x == x) and (n_y == y) and (n_z == z) and (n_w == w):
                        continue
                    if is_active(n_x, n_y, n_z, n_w, pocket_dimension, min_max):
                        count += 1
    return count


def is_active(x, y, z, w, pocket_dimension, min_max=None):
    if min_max:
        if (x <= min_max["x"][0]) or (x >= min_max["x"][1]) or (y <= min_max["y"][0]) or (y >= min_max["y"][1]) or (z <= min_max["z"][0]) or (z >= min_max["z"][1]) or (w <= min_max["w"][0]) or (w >= min_max["w"][1]):
            return False
    if pocket_dimension.get((x, y, z, w)) == "#":
        return True
    return False


def do_six_cycles(pocket_dimension, total_dimension=3):
    spaces = " " * 6
    for i in range(6):
        pocket_dimension = do_cycle(pocket_dimension, total_dimension=total_dimension)
        if total_dimension == 4:
            final_message = "Complete" if i == 5 else f"{i+1}/6"
            print(f"{spaces}Part 2: {final_message}")
    count = 0
    for cube in pocket_dimension:
        if is_active(*cube, pocket_dimension):
            count += 1
    if total_dimension == 3:
        print(f"\n{spaces}Part 1: Complete")
    return count


#############
#  answers  #
#############

def get_answer_1(pocket_dimension):
    time_start = time.perf_counter()
    count = do_six_cycles(pocket_dimension)
    time_spent = time.perf_counter() - time_start
    return {"value": count, "time": time_spent}


def get_answer_2(pocket_dimension):
    time_start = time.perf_counter()
    count = do_six_cycles(pocket_dimension, total_dimension=4)
    time_spent = time.perf_counter() - time_start
    return {"value": count, "time": time_spent}


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
    puzzle_input = get_data_from_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
