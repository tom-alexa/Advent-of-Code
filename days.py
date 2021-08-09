
# script prints all days that user can use

# constants
FIRST_YEAR = 2015
LAST_YEAR = 2020

FIRST_DAY = 1
LAST_DAY = 25

# spaces
YEAR_INDENTATION = " " * 4
DAY_INDENTATION = " " * 8

# days
COMPLETED_DAYS = {
    2020: {
        1,
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
    for year in days:
        for day in days[year]:
            if days[year][day]:
                if year != last_year:
                    last_year = year
                    text_to_print += f"\n{YEAR_INDENTATION}-> {last_year}\n"
                text_to_print += f"{DAY_INDENTATION}> {day:>2}  >>  python {year}/{day:02}/main.py\n"
    return text_to_print


def main():
    days = create_days_dictionary()
    update_by_completed_days(days)
    print(get_text_to_print(days))


if __name__ == "__main__":
    main()
