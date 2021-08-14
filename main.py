import os
from pathlib import PurePath

INDENTATION = " " * 2
TO_REMEMBER = "src/to_remember"
FILE_NAME = "solution.py"


def get_last_used_data():
    with open(TO_REMEMBER, "r") as file:
        lines = []
        for line in file.readlines():
            if "year" in line:
                try:
                    remembered_year = int(line.split(":")[-1].strip())
                except ValueError:
                    remembered_year = None
                continue
            elif "day" in line:
                try:
                    remembered_day = int(line.split(":")[-1].strip())
                    continue
                except ValueError:
                    remembered_day = None
                continue
            lines.append(line)
    return {"lines": lines, "year": remembered_year, "day": remembered_day}


def get_file(data, file_name):
    remembered_year = data["year"]
    remembered_day = data["day"]
    print()
    if remembered_year:
        while True:
            try:
                year = input(f"{INDENTATION*2}Year [{remembered_year}]: ")
                year = int(year) if year else remembered_year
                break
            except ValueError:
                print(f"{INDENTATION*3}↑ has to be a number!\n")
    else:
        while True:
            try:
                year = int(input(f"{INDENTATION*2}Year: "))
                if year:
                    break
            except ValueError:
                print(f"{INDENTATION*3}↑ has to be a number!\n")
    if remembered_day:
        while True:
            try:
                day = input(f"{INDENTATION*2}Day [{remembered_day}]: ")
                day = int(day) if day else remembered_day
                break
            except ValueError:
                print(f"{INDENTATION*3}↑ has to be a number!\n")
    else:
        while True:
            try:
                day = int(input(f"{INDENTATION*2}Day: "))
                if day:
                    break
            except ValueError:
                print(f"{INDENTATION*3}↑ has to be a number!\n")
    data["year"] = year
    data["day"] = day
    return PurePath(f"{year:04}/{day:02}/{file_name}")


def update_last_data(data, file_path):
    year = data["year"]
    day = data["day"]
    with open(file_path, "w") as file:
        file.write(f"year: {year}\n")
        file.write(f"day: {day}\n")
        for line in data["lines"]:
            file.write(line)


def start_script(file):
    os.system(f"python {file}")


def main():
    data = get_last_used_data()
    solution_file = get_file(data, FILE_NAME)
    update_last_data(data, TO_REMEMBER)
    start_script(solution_file)


if __name__ == "__main__":
    main()
