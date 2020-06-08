#!/usr/bin/env python3
import csv
import datetime

FILE = "employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print("Getting the first start date to query for.")
    print()
    print("The date must be greater than Jan 1st, 2018")
    year = int(input("Enter a value for the year: "))
    month = int(input("Enter a value for the month: "))
    day = int(input("Enter a value for the day: "))
    print()
    return datetime.datetime(year, month, day)


def get_file_lines(csvfile):
    """Returns the lines contained in the file"""
    with open(csvfile, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def list_newer(start_date):
    """parse CSV rows for given start date"""
    data = get_file_lines(FILE)
    employees = {}
    for row in data:
        row_name = "{} {}".format(row["first_name"], row["last_name"])
        employees.setdefault(row["start_date"], []).append(row_name)

    start_dates = sorted(employees.keys())
    for date in start_dates:
        employee_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        if employee_date >= start_date:
            print(
                "Started on {}: {}".format(
                    employee_date.strftime("%b %d, %Y"), employees[date]
                )
            )


def main():
    start_date = get_start_date()
    list_newer(start_date)


if __name__ == "__main__":
    main()
