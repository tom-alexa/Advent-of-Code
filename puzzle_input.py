import os
from main import INDENTATION, TO_REMEMBER, get_file

FILE_NAME = "input"


def get_last_used_data():
    with open(TO_REMEMBER, "r") as file:
        lines = []
        for line in file.readlines():
            if "editor" in line:
                editor = line.split(":")[-1].strip()
                continue
            elif "year" in line:
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
    return {"lines": lines, "editor": editor, "year": remembered_year, "day": remembered_day}


def get_editor(data):
    remembered_editor = data["editor"]
    if remembered_editor:
        editor = input(f"\n{INDENTATION*2}Editor [{remembered_editor}]: ")
        editor = editor if editor else remembered_editor
    else:
        print(f"\n{INDENTATION}You have NOT define your text editor yet, type your text editor!")
        while True:
            editor = input(f"{INDENTATION*2}Editor: ")
            if editor:
                data["editor"] = editor
                break
    return editor


def update_last_data(data, file_path):
    editor = data["editor"]
    year = data["year"]
    day = data["day"]
    with open(file_path, "w") as file:
        file.write(f"editor: {editor}\n")
        file.write(f"year: {year}\n")
        file.write(f"day: {day}\n")
        for line in data["lines"]:
            file.write(line)


def open_editor(editor, file):
    os.system(f"{editor} {file}")


def main():
    data = get_last_used_data()
    input_file = get_file(data, FILE_NAME)
    editor = get_editor(data)
    update_last_data(data, TO_REMEMBER)
    open_editor(editor, input_file)


if __name__ == "__main__":
    main()
