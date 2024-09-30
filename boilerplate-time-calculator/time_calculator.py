import re


def add_time(start, duration, start_day=None):
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]

    split_1 = re.split(":", start)
    split_2 = re.split(" ", split_1[1])

    hours = int(split_1[0])
    minutes = int(split_2[0])

    period = split_2[1]
    if period == "PM" and hours != 12:
        hours += 12
    if hours == 12 and period == "AM":
        hours = 0

    split_3 = re.split(":", duration)
    hours_to_add = int(split_3[0])
    minutes_to_add = int(split_3[1])

    minutes += minutes_to_add
    hours += minutes // 60
    minutes = minutes % 60

    hours += hours_to_add
    days = hours // 24
    hours = hours % 24

    new_period = "AM"
    if hours >= 12:
        new_period = "PM"
        hours -= 12
        
    if hours == 0:
        hours += 12

    new_time = str(hours) + ":" + str(minutes).zfill(2) + " " + new_period
    if start_day:
        start_day = start_day.capitalize()
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days) % 7
        new_time += ", " + days_of_week[new_day_index]

    if days == 1:
        new_time += " (next day)"
    elif days > 1:
        new_time += " (" + str(days) + " days later)"

    return new_time
