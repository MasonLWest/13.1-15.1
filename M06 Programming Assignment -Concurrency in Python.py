from datetime import date, datetime, timedelta

# write the current date to today.txt
today = date.today().strftime("%Y-%m-%d")

with open('today.txt', 'w') as f:
    f.write(today)

# read the text file today.txt into the string today_string
with open('today.txt', 'r') as f:
    today_string = f.read()

# parse the date from today_string
parsed_date = datetime.strptime(today_string, '%Y-%m-%d')

# create a date object of your day of birth
birthday = date(year, month, day)  # replace year, month, and day with your actual birth date

# find out the day of the week of your day of birth
day_of_week = birthday.strftime("%A")

# find out when you will be (or when you were) 10,000 days old
ten_thousand_days = timedelta(days=10000)
ten_thousand_days_old = birthday + ten_thousand_days
