import pandas as pd

holidayFile = "data/holidays.txt"
# def get_holidays(fpath):
    # holidays are from http://www.timeanddate.com/holidays/us/ , holidays and some observances

f = open(holidayFile)
lines = f.readlines()
lines = [line.split(" ")[:3] for line in lines]
lines = ["{} {} {}".format(line[0], line[1], line[2]) for line in lines]
lines = pd.to_datetime(lines)

holidays = pd.DataFrame({"date2":lines})
print(holidays)

# holiday_names are holidays + around Black Fridays

holidayNameFile = "data/holiday_names.txt"
f = open(holidayNameFile)
lines = f.readlines()
lines = [line.strip().split(" ")[:4] for line in lines]
lines_dt = ["{} {} {}".format(line[0], line[1], line[2]) for line in lines]
lines_dt = pd.to_datetime(lines_dt)
lines_hol = [line[3] for line in lines]

holidayNames = pd.DataFrame({"date2": lines_dt, "holiday_name": lines_hol})
print(holidayNames)