from datetime import datetime


def main():
    input_year = int(input())
    is_black_friday(year=input_year)


def is_black_friday(year):
    no_result = True
    for month in range(1, 13):
        date = datetime(year=year, month=month, day=13)
        if date.weekday() == 4:
            date_string = date.strftime("%Y-%m-%d")
            print(date_string)
            no_result = False
    if no_result:
        print("None")


if __name__ == "__main__":
    main()
