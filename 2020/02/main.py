import time

# --- Day 2: Password Philosophy ---


###########
#  input  #
###########

def get_data_from_input():
    with open("2020/02/input", "r") as file:
        password_database = []
        for line in file.readlines():
            terms, password_string = map(lambda x: x.strip(), line.split(":"))
            key, letter = terms.split(" ")
            k_min, k_max = map(int, key.split("-"))
            password_database.append({"password": password_string, "terms": {"letter": letter, "key": {"min": k_min, "max": k_max}}})
    return password_database


#############
#  answers  #
#############

def get_answer_1(password_database):
    time_start = time.perf_counter()
    valid_passwords = []
    for password in password_database:
        password_string = password["password"]
        letter = password["terms"]["letter"]
        k_min = password["terms"]["key"]["min"]
        k_max = password["terms"]["key"]["max"]

        key_letter_total = password_string.count(letter)
        if key_letter_total >= k_min and key_letter_total <= k_max:
            valid_passwords.append(password)

    time_spent = time.perf_counter() - time_start
    return {"value": len(valid_passwords), "time": time_spent}


def get_answer_2(password_database):
    time_start = time.perf_counter()
    valid_passwords = []
    for password in password_database:
        password_string = password["password"]
        letter = password["terms"]["letter"]
        k_min = password["terms"]["key"]["min"]
        k_max = password["terms"]["key"]["max"]

        contain = 0
        if password_string[k_min-1] == letter:
            contain += 1
        if password_string[k_max-1] == letter:
            contain += 1
        if contain == 1:
            valid_passwords.append(password)

    time_spent = time.perf_counter() - time_start
    return {"value": len(valid_passwords), "time": time_spent}


##########
#  main  #
##########

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
    print(f"\n{indetation}2020 > 02")
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
