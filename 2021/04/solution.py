import time
from pathlib import PurePath

# --- Day 4: Giant Squid ---


###############
#  constants  #
###############

YEAR = 2021
DAY = 4

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")


###########
#  input  #
###########

def get_data_from_input():
    game = {}
    with open(INPUT_FILE, "r") as file:
        lines = file.read().split("\n\n")
        game["turns"] = [int(number) for number in lines[0].split(",")]
        game["boards"] = []
        for board in lines[1:]:
            game["boards"].append(
                list(map(
                    lambda x: list(map(
                        int, filter(lambda y: y.isnumeric(), x.split(" ")))),
                        board.split("\n")))
            )
    return game


###############
#  functions  #
###############

def to_sets(boards):
    rows_and_columns = []
    for board in boards:
        rows = list(map(lambda x: set(x), board))
        columns = []
        for i in range(5):
            cur_col = set()
            for row in board:
                cur_col.add(row[i])
            columns.append(cur_col)
        rows_and_columns.append(rows + columns)
    return rows_and_columns


def play_to_win(turns, boards):
    for turn in turns:
        for board in boards:
            for row_or_column in board:
                row_or_column.discard(turn)
                if not row_or_column:
                    return sum_of_unmarked(board, turn) * turn


def play_to_lose(turns, boards):
    last_to_win = False
    for turn in turns:
        delete = []
        for i, board in enumerate(boards):
            for row_or_column in board:
                row_or_column.discard(turn)
                if not row_or_column:
                    if last_to_win:
                        return sum_of_unmarked(board, turn) * turn
                    delete.append(i)
                    break
        for i, index in enumerate(delete[::-1]):
            del boards[index - i]
        if len(boards) == 1:
            last_to_win = True


def sum_of_unmarked(board, turn):
    unmarked_numbers = set()
    for roc in board:
        unmarked_numbers.update(roc)
    unmarked_numbers.discard(turn)
    return sum(unmarked_numbers)


#############
#  answers  #
#############

def get_answer_1(game):
    time_start = time.perf_counter()
    boards = to_sets(game["boards"][:])
    score = play_to_win(game["turns"], boards)
    time_spent = time.perf_counter() - time_start
    return {"value": score, "time": time_spent}


def get_answer_2(game):
    time_start = time.perf_counter()
    boards = to_sets(game["boards"][:])
    score = play_to_lose(game["turns"], boards)
    time_spent = time.perf_counter() - time_start
    return {"value": score, "time": time_spent}


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
