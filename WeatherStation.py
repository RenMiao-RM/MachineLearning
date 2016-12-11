import pandas as pd

inputFile = 'Data/trainNoZeroWithWeekdayIsHoliday.csv'
keyFile = 'Data/key.csv'
weatherFile = 'Data/weather.csv'
outputFile = 'Data/dataWithStation.csv'

inputData = pd.read_csv(inputFile)
keyData = pd.read_csv(keyFile)
weatherData = pd.read_csv(weatherFile)
inputData.insert(5, 'station_nbr', 0)

# print(inputData)

for index, row in inputData.iterrows():
    # find the station # according to the store #
    storeNum = row['store_nbr']
    stationNum = (keyData[keyData['store_nbr'] == storeNum]).iloc[0]['station_nbr']
    # print(stationNum)
    inputData.set_value(index, 'station_nbr', stationNum)

    # dateInfo = row['date']
    # dateArr = dateInfo.split('-')
    # year = (int)(dateArr[0])
    # month = (int)(dateArr[1])
    # day = (int)(dateArr[2])

inputData.to_csv(outputFile)
