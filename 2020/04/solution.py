import time
from pathlib import PurePath

# --- Day 4: Passport Processing ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 4

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input.txt")

PROPERTIES = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
NOT_COMPULSORY_PROPERTIES = {"cid"}

BIRTH_YEAR = {"min": 1920, "max": 2002}
ISSUE_YEAR = {"min": 2010, "max": 2020}
EXPIRATION_YEAR = {"min": 2020, "max": 2030}
HEIGHT = {"cm": {"min": 150, "max": 193}, "in": {"min": 59, "max": 76}}
EYE_COLOR = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
PASSPORT_ID = {"length": 9}


###########
#  input  #
###########

def get_data_from_input():
    passports = []
    with open(INPUT_FILE, "r") as file:
        passports_dirty = file.read().split("\n\n")
        for current_passport in passports_dirty:
            passport = {}
            for compulsory_property in PROPERTIES:
                passport[compulsory_property] = None
            property_dirty = current_passport.split("\n")
            for property_half_dirty in property_dirty:
                property_almost = property_half_dirty.split(" ")
                for passport_property in property_almost:
                    if passport_property:
                        key, value = passport_property.split(":")
                        passport[key] = value
            passports.append(passport)
    return passports


###############
#  functions  #
###############

def check_byr(birth_yr):
    if not birth_yr:
        return False
    birth_yr = int(birth_yr)
    if birth_yr < BIRTH_YEAR["min"] or birth_yr > BIRTH_YEAR["max"]:
        return False
    return True


def check_iyr(issue_yr):
    if not issue_yr:
        return False
    issue_yr = int(issue_yr)
    if issue_yr < ISSUE_YEAR["min"] or issue_yr > ISSUE_YEAR["max"]:
        return False
    return True


def check_eyr(expiration_yr):
    if not expiration_yr:
        return False
    expiration_yr = int(expiration_yr)
    if expiration_yr < EXPIRATION_YEAR["min"] or expiration_yr > EXPIRATION_YEAR["max"]:
        return False
    return True


def check_hgt(hght):
    if not hght:
        return False
    if len(hght) < 2:
        return False
    hght_unit = hght[-2:]
    if hght_unit != "cm" and hght_unit != "in":
        return False
    hght_value = int(hght[:-2])
    if hght_unit == "cm":
        if hght_value < HEIGHT["cm"]["min"] or hght_value > HEIGHT["cm"]["max"]:
            return False
    else:
        if hght_value < HEIGHT["in"]["min"] or hght_value > HEIGHT["in"]["max"]:
            return False
    return True


def check_hcl(hair_clr):
    if not hair_clr:
        return False
    if len(hair_clr) != 7 or hair_clr[0] != "#":
        return False
    possible_letters = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
    for i in range(1, 7):
        letter = hair_clr[i]
        if letter not in possible_letters:
            return False
    return True


def check_ecl(eye_clr):
    if eye_clr not in EYE_COLOR:
        return False
    return True


def check_pid(pssprt_id):
    if not pssprt_id:
        return False
    if len(pssprt_id) != 9:
        return False
    return True


#############
#  answers  #
#############

def get_answer_1(passports):
    time_start = time.perf_counter()
    valid_passports = []
    for passport in passports:
        valid = True
        for passport_property in passport:
            if not passport[passport_property] and passport_property not in NOT_COMPULSORY_PROPERTIES:
                valid = False
                break
        if valid:
            valid_passports.append(passport)
    time_spent = time.perf_counter() - time_start
    return {"value": len(valid_passports), "time": time_spent}


def get_answer_2(passports):
    time_start = time.perf_counter()
    valid_passports = []
    for passport in passports:
        if not check_byr(passport["byr"]):
            continue
        if not check_iyr(passport["iyr"]):
            continue
        if not check_eyr(passport["eyr"]):
            continue
        if not check_hgt(passport["hgt"]):
            continue
        if not check_hcl(passport["hcl"]):
            continue
        if not check_ecl(passport["ecl"]):
            continue
        if not check_pid(passport["pid"]):
            continue
        valid_passports.append(passport)

    time_spent = time.perf_counter() - time_start
    return {"value": len(valid_passports), "time": time_spent}


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
