import sys
import datetime
import csv

def get_all_sundays(year):
    # January 1st of the given year
    dt = datetime.date(year, 1, 1)
    # Move to the first Sunday
    dt += datetime.timedelta(days=(6 - dt.weekday()))
    while dt.year == year:
        yield dt
        dt += datetime.timedelta(weeks=1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python sundays.py <year>")
        return

    try:
        year = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid year.")
        return

    sundays = list(get_all_sundays(year))
    filename = f"sundays_{year}.csv"

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sunday Dates"])
        for sunday in sundays:
            writer.writerow([sunday])

    print(f"Sundays of {year} have been saved to {filename}.")

if __name__ == "__main__":
    main()
