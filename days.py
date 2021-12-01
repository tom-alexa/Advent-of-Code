
# script prints all days that user can use

# constants
FIRST_YEAR = 2015
LAST_YEAR = 2021

FIRST_DAY = 1
LAST_DAY = 25

# spaces
YEAR_INDENTATION = " " * 4
DAY_INDENTATION = " " * 8

# days
COMPLETED_DAYS = {
    2020: {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    },
    2021: {
        1
    },
}


def create_days_dictionary():
    days = {}
    for year in range(FIRST_YEAR, LAST_YEAR+1):
        days[year] = {}

        for day in range(FIRST_DAY, LAST_DAY+1):
            days[year][day] = False
    return days


def update_by_completed_days(days):
    for year in COMPLETED_DAYS:
        for day in COMPLETED_DAYS[year]:
            days[year][day] = True


def get_text_to_print(days):
    text_to_print = ""
    last_year = None
    line_breaks = 0
    for year in days:
        for day in days[year]:
            if days[year][day]:
                if year != last_year:
                    last_year = year
                    text_to_print += f"\n\n{YEAR_INDENTATION}-> {last_year}\n{DAY_INDENTATION}> "
                if day > 10 and line_breaks < 1:
                    line_breaks += 1
                    text_to_print += f"\n{DAY_INDENTATION}> "
                elif day > 20 and line_breaks < 2:
                    line_breaks += 1
                    text_to_print += f"\n{DAY_INDENTATION}> "
                text_to_print += f"{day:>2} | "
    return text_to_print + "\n"


def main():
    days = create_days_dictionary()
    update_by_completed_days(days)
    print(get_text_to_print(days))


if __name__ == "__main__":
    main()
