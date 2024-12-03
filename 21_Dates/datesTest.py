from datetime import datetime, date, timedelta


# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Current date only
today = date.today()
print("Today's Date:", today)

# Current year, month, and day
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Formatting a date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Common formatting codes:
# %Y - Year (e.g., 2023)
# %m - Month (01 to 12)
# %d - Day (01 to 31)
# %H - Hour (00 to 23)
# %M - Minute (00 to 59)
# %S - Second (00 to 59)

date_string = "2024-12-01 15:45:30"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed_date)

# Yesterday
yesterday = today - timedelta(days=1)
print("Yesterday:", yesterday)

# Tomorrow
tomorrow = today + timedelta(days=1)
print("Tomorrow:", tomorrow)

# Adding 7 days
next_week = today + timedelta(days=7)
print("Next Week:", next_week)

#6. Calculating the Difference Between Dates
date1 = datetime(2024, 12, 1)
date2 = datetime(2024, 11, 25)
difference = date1 - date2
print("Difference:", difference.days, "days")

#7. Extracting Specific Parts of a Date

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

#Woeking with timezone

import pytz

# Current time in UTC
utc_now = datetime.now(pytz.utc)
print("Current UTC Time:", utc_now)

# Convert UTC to another timezone
india_time = utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
print("India Time:", india_time)

#9. Leap Year Check

import calendar

year = 2024
is_leap = calendar.isleap(year)
print(f"Is {year} a leap year? {is_leap}")


custom_date = datetime(2024, 12, 25, 10, 30, 0)
print("Custom Date:", custom_date)
