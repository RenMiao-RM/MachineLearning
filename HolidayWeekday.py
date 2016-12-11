import pandas as pd
import datetime
import holidays

trainFileNoZero = "Data/trainNoZero.csv"
saveFile = 'Data/trainNoZeroWithWeekdayIsHoliday.csv'

trainData = pd.read_csv(trainFileNoZero)

# get rid of the extra column
trainData = trainData.drop('Unnamed: 0', 1)
trainData.insert(1, 'weekday', 0)
trainData.insert(2, 'isHoliday', 0)

us_holidays = holidays.UnitedStates()

for index, row in trainData.iterrows():
    dateRow = row['date']
    dateArr = dateRow.split('-')
    year = (int)(dateArr[0])
    month = (int)(dateArr[1])
    day = (int)(dateArr[2])

    dateObject = datetime.date(year, month, day)
    weekday = dateObject.weekday()
    isHoliday = dateObject in us_holidays

    trainData.set_value(index, 'weekday', weekday)
    trainData.set_value(index, 'isHoliday', isHoliday)

print(trainData)
# trainData.to_csv(saveFile)