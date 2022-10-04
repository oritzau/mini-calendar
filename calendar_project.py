#returns first day of given year
def first_day_of_year(year):
    return int((2 + (year-1901) + (year-1901)/4) % 7)

#returns day in words
def day_num_to_words(day_num):
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_in_words = day_list[day_num]
    return day_in_words

#returns month in words
def month_num_to_words(month_num):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month_list[month_num - 1]

#returns first day of month as number
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

#returns number of days in month
def num_of_days(month_num, year):
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_num != 2:
        return days_in_month_list[month_num - 1]
    elif month_num == 2:
        if year % 4 == 0:
            return 29
        else:
            return days_in_month_list[month_num - 1]

#takes year and month as arguments and prints calendar info
if __name__ == "__main__":
    month = int(input('Month: '))
    while month < 0 or month > 12:
        print('Month must be between 1 and 12')
        month = int(input('Month: '))
    year = int(input('Year: '))

    first_day = first_day_of_year(year)
    print('\n')
    print(f'The first day of {month_num_to_words(month)} is on a {day_num_to_words(first_day_month_in_year(year, month))} \n')
    print(f'The first day of {year} is on a {day_num_to_words(first_day)}\n')
    print(f'{month_num_to_words(month)} has {num_of_days(month,year)} days')
 