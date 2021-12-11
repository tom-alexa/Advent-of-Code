import time
from pathlib import PurePath

# --- Day 5: Hydrothermal Venture ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 5

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def parse_input():
    vectors = []
    with open(INPUT_FILE, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            (x_1, y_1), (x_2, y_2) = map(lambda x: x.split(","), line.split(" -> "))
            vectors.append({"A": (int(x_1), int(y_1)), "B": (int(x_2), int(y_2))})
    return vectors


###############
#  functions  #
###############

def start_end(vector):
    start_x = vector["A"][0]
    end_x = vector["B"][0]
    if vector["A"][0] > vector["B"][0]:
        start_x, end_x = end_x, start_x
    start_y = vector["A"][1]
    end_y = vector["B"][1]
    if vector["A"][1] > vector["B"][1]:
        start_y, end_y = end_y, start_y
    return start_x, end_x, start_y, end_y


def loop_vectors(vectors, diagonal=False):
    mapper = {}
    count = 0
    for vector in vectors:
        if not (vector["A"][0] == vector["B"][0] or vector["A"][1] == vector["B"][1]):                              # horizontal, vertical
            if (not diagonal) or (abs(vector["A"][0] - vector["B"][0]) != abs(vector["A"][1] - vector["B"][1])):    # diagonal
                continue
        start_x, end_x, start_y, end_y = start_end(vector)
        if not diagonal or (vector["A"][0] == vector["B"][0] or vector["A"][1] == vector["B"][1]):                  # horizontal, vertical
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    mapper[(x, y)] = mapper.setdefault((x, y), 0) + 1
                    if mapper[(x, y)] == 2:
                        count += 1
        else:                                                                                                       # diagonal
            for i in range(end_x - start_x + 1):
                if vector["A"][0] == start_x:
                    if vector["A"][1] == start_y:
                        x, y = vector["A"][0] + i, vector["A"][1] + i
                    else:
                        x, y = vector["A"][0] + i, vector["A"][1] - i
                else:
                    if vector["A"][1] == start_y:
                        x, y = vector["A"][0] - i, vector["A"][1] + i
                    else:
                        x, y = vector["A"][0] - i, vector["A"][1] - i
                mapper[(x, y)] = mapper.setdefault((x, y), 0) + 1
                if mapper[(x, y)] == 2:
                    count += 1
    return count


#############
#  answers  #
#############

def get_answer_1(vectors):
    time_start = time.perf_counter()
    count = loop_vectors(vectors)
    time_spent = time.perf_counter() - time_start
    return {"value": count, "time": time_spent}


def get_answer_2(vectors):
    time_start = time.perf_counter()
    count = loop_vectors(vectors, diagonal=True)
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
    puzzle_input = parse_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()
