import pandas as pd
import datetime
import holidays

inputFile = "Data/testProcessed_0.csv"
outputFile = 'Data/testProcessed_1.csv'

inputData = pd.read_csv(inputFile)

# get rid of the extra column
inputData = inputData.drop('Unnamed: 0', 1)
inputData.insert(1, 'isWeekend', 0)
inputData.insert(2, 'isHoliday', 0)

us_holidays = holidays.UnitedStates()

for index, row in inputData.iterrows():
    dateRow = row['date']
    dateArr = dateRow.split('-')
    year = (int)(dateArr[0])
    month = (int)(dateArr[1])
    day = (int)(dateArr[2])

    dateObject = datetime.date(year, month, day)
    weekday = dateObject.weekday()
    isWeekend = 0
    if weekday == 5 or weekday == 6:
        isWeekend = 1
    isHoliday = dateObject in us_holidays

    inputData.set_value(index, 'isWeekend', isWeekend)
    inputData.set_value(index, 'isHoliday', isHoliday)

print(inputData)
inputData.to_csv(outputFile)