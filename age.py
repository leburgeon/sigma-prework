import datetime
import math


def get_date_age(input_date):
    date_values = input_date.strip().split('-')

    if len(date_values) != 3:
        return 'Invalid Input'

    try:
        for i, arg in enumerate(date_values):
            date_values[i] = int(arg)
        date_to_age = datetime.date(
            date_values[2], date_values[1], date_values[0])
    except:
        return 'Invalid Input'

    time_delta_difference = date_to_age - datetime.date.today()

    return math.floor(time_delta_difference.days / 365)


def main():
    # Main prog loop
    while True:

        date = input('Please enter a date to age (dd-mm-yyyy):')

        age = get_date_age(date)

        if type(age) == str:
            print(age)
        elif age < 0:
            print(f'{date} was {abs(age)} year(s) ago!')
        elif age > 0:
            print(f'{date} is in {age} year(s)!')
        else:
            print(f'{date} is less than a year from now!')


if __name__ == '__main__':
    main()
