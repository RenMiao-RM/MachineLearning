# Add 3 more weather features into the test file (snowfall, preciptotal, avewindspeed)

import pandas as pd

inputFile = 'Data/testProcessed_2.csv'
# keyFile = 'Data/key.csv'
weatherFile = 'Data/weather.csv'
outputFile = 'Data/testProcessed_3.csv'

inputData = pd.read_csv(inputFile)
inputData = inputData.drop('Unnamed: 0', 1)
# inputData = inputData.drop('Unnamed: 0.1', 1)
inputData.insert(1, 'SnowFall', 0)
inputData.insert(1, 'PrecipTotal', 0)
inputData.insert(1, 'aveWindSpeed', 0)
inputData[['SnowFall', 'PrecipTotal', 'aveWindSpeed']] = inputData[['SnowFall', 'PrecipTotal', 'aveWindSpeed']].astype(float)

weatherData = pd.read_csv(weatherFile)

for index, row in inputData.iterrows():
    if row['units'] != 0:
    # find the station # according to the store #
        stationNum = row['station_nbr']
        dateInfo = row['date']
        # print(stationNum)

        weatherRow = weatherData[(weatherData['station_nbr'] == stationNum) & (weatherData['date'] == dateInfo)]

        snowFall = weatherRow.iloc[0]['snowfall']
        try:
            snowFall = float(snowFall)
        except ValueError:
            snowFall = 0

        inputData.set_value(index, 'SnowFall', snowFall)

        precipTotal = weatherRow.iloc[0]['preciptotal']
        # if precipTotal == 'M' or precipTotal == 'T':
        #     precipTotal = 0
        try:
            precipTotal = float(precipTotal)
        except ValueError:
            precipTotal = 0

        inputData.set_value(index, 'PrecipTotal', precipTotal)

        aveSpeed = weatherRow.iloc[0]['avgspeed']
        try:
            aveSpeed = float(aveSpeed)
        except ValueError:
            aveSpeed = 0

        inputData.set_value(index, 'aveWindSpeed', aveSpeed)

inputData.to_csv(outputFile, index=False)
