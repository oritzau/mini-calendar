
def first_day_of_year(year):
    return int((2 + (year-1901) + (year-1901)/4) % 7)

def day_num_to_words(day_num):
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_in_words = day_list[day_num]
    return day_in_words

def month_num_to_words(month_num):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_list[month_num - 1]

def first_day_month_in_year(year, month):
    first_day_of_year = int((2 + (year-1901) + (year-1901)/4) % 7)
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    first_day_month_in_year = first_day_of_year
    counter = 0
    while counter < month - 1:
        if counter == 1:
            if year % 4 == 0:
                first_day_month_in_year += 29
                counter += 1
            else:
                first_day_month_in_year += 28
                counter += 1
        else:
            first_day_month_in_year += days_in_month_list[counter]
            counter += 1
    return first_day_month_in_year % 7

def num_of_days(month_num, year):
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_num != 2:
        return days_in_month_list[month_num - 1]
    elif month_num == 2:
        if year % 4 == 0:
            return 29
        else:
            return days_in_month_list[month_num - 1]
def print_calendar(day_num, days_in_month_num):
    top_str = month_num_to_words(month) + ', ' + str(year)
    top_str = f'{top_str:^22}'
    print(top_str)
    calendar_str = 'Su Mon Tu We Th Fr Sa'
    print(calendar_str)
    day_printed = 1
    counter = 1
    space = ''
    while counter < day_num:
        print(f'{space:3}', end = '')
        counter += 1
    while counter >= day_num and day_printed <= days_in_month_num:
        if counter % 7 == 0:
            print(f'{day_printed:3}')
        else:
            print(f'{day_printed:3}', end = '')
        counter += 1
        day_printed += 1

if __name__ == "__main__":
    month = int(input('Month: '))
    while month < 0 or month > 12:
        print('Month must be between 1 and 12')
        month = int(input('Month: '))
    year = int(input('Year: '))

    first_day = first_day_of_year(year)
    print()
    print_calendar(first_day_month_in_year(year, month), num_of_days(month, year))
