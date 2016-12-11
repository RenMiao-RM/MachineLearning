#add three more weather features (snow fall, precipitation total and average wind speed into the train data set)

import pandas as pd

inputFile = 'Data/finalTrain_0.csv'
weatherFile = 'Data/weather.csv'
outputFile = 'Data/finalTrain_1.csv'

inputData = pd.read_csv(inputFile)
inputData = inputData.drop('Unnamed: 0', 1)
inputData = inputData.drop('Unnamed: 0.1', 1)
inputData.insert(1, 'SnowFall', 0)
inputData.insert(1, 'PrecipTotal', 0)
inputData.insert(1, 'aveWindSpeed', 0)
inputData[['SnowFall', 'PrecipTotal', 'aveWindSpeed']] = inputData[['SnowFall', 'PrecipTotal', 'aveWindSpeed']].astype(float)

weatherData = pd.read_csv(weatherFile)

# print(inputData)

for index, row in inputData.iterrows():
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