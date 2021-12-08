import time
from pathlib import PurePath

# --- Day 8: Seven Segment Search ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 8

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        lines = [line.split(" | ") for line in file.readlines()]
        segments = []
        for line in lines:
            part_list = []
            for part in line:
                part_list.append([x.strip() for x in part.split(" ")])
            segments.append(part_list)
    return segments


#############
#  answers  #
#############

def get_answer_1(segments):
    time_start = time.perf_counter()

    total = 0
    for line in segments:
        for segment in line[1]:
            if len(segment) in [2, 4, 3, 7]:  # numbers: 1, 4, 7, 8
                total += 1

    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


def get_answer_2(segments):
    time_start = time.perf_counter()

    total = 0
    for line in segments:
        eight, *unsolved, four, seven, one = sorted(line[0], key=len, reverse=True)
        eight, four, seven, one = set(eight), set(four), set(seven), set(one)
        for uns in unsolved:
            uns = set(uns)
            if len(uns) == 6:
                if len(uns - one) != 4:
                    six = uns
                elif len(uns - four) == 2:
                    nine = uns
                else:
                    zero = uns
            else:
                if len(uns - seven) == 2:
                    three = uns
                elif len(six - uns) == 1:
                    five = uns
                else:
                    two = uns

        output_value = ""
        for output in line[1]:
            s_out = set(output)
            if s_out == zero:
                output_value += "0"
            elif s_out == one:
                output_value += "1"
            elif s_out == two:
                output_value += "2"
            elif s_out == three:
                output_value += "3"
            elif s_out == four:
                output_value += "4"
            elif s_out == five:
                output_value += "5"
            elif s_out == six:
                output_value += "6"
            elif s_out == seven:
                output_value += "7"
            elif s_out == eight:
                output_value += "8"
            elif s_out == nine:
                output_value += "9"
        total += int(output_value)

    time_spent = time.perf_counter() - time_start
    return {"value": total, "time": time_spent}


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
