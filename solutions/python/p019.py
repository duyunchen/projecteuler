"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# We start at 1 Jan 1990 and just go up counting sundays while following all the
# rules with regards to leap years and days per month and whatnot
def run():
    curr_day, curr_month, curr_year = 1,1,1900
    
    num_sundays = 0
    day_count = 0
    
    while (curr_day, curr_month, curr_year) != (31, 12, 2000):
        if curr_year >= 1901 and day_count % 7 == 0 and curr_day == 1:
            num_sundays += 1
            
        if is_last_day_of_month(curr_year, curr_month, curr_day):
            curr_day = 1
            curr_month += 1
            if curr_month > 12:
                curr_month = 1
                curr_year += 1
        else:
            curr_day += 1
        day_count += 1
                
    return num_sundays
        
def is_last_day_of_month(year, month, day):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4,6,9,11]:
        return day == 30
    else:
        return day == 31
    
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
   

