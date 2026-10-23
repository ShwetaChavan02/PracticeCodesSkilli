# convert american time to indian time
# Given a date and time in American Time, convert it into Indian Standard Time (IST).
# For this problem, assume that the given American time is exactly 9 hours 30 minutes behind Indian time.
# You are given three integers:
# day — the day of the month hours — the hour in 24-hour format minutes — the minutes
# Add 9 hours and 30 minutes to the given time.
# If the resulting time goes beyond 23:59, move to the next day and adjust the hour accordingly.
# Rules:-
# If the resulting time is before midnight on the same day, return the updated day, hour, and minutes.
# If the resulting time reaches or passes midnight, increment the day by 1 and adjust the hour accordingl


def convertTime(day: int, hours: int, minutes: int) -> list[int]:
    if day < 1 or hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return [-1, -1, -1]
    minutes = minutes + 30
    hours = hours + 9
    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
    if hours >= 24:
        hours = hours - 24
        day = day + 1
    return [day, hours, minutes]