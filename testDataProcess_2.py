# Add weather information into the test file

import pandas as pd

inputFile = 'Data/testProcessed_1.csv'
keyFile = 'Data/key.csv'
weatherFile = 'Data/weather.csv'
outputFile = 'Data/testProcessed_2.csv'

inputData = pd.read_csv(inputFile)
keyData = pd.read_csv(keyFile)
weatherData = pd.read_csv(weatherFile)
inputData.insert(5, 'station_nbr', 0)
inputData.insert(6, 'temp depart', 0)

# print(inputData)

for index, row in inputData.iterrows():
    if row['units'] != 0:
    # find the station # according to the store #
        storeNum = row['store_nbr']
        stationNum = (keyData[keyData['store_nbr'] == storeNum]).iloc[0]['station_nbr']
        # print(stationNum)
        inputData.set_value(index, 'station_nbr', stationNum)

        dateInfo = row['date']

        weatherRow = weatherData[(weatherData['station_nbr'] == stationNum) & (weatherData['date'] == dateInfo)]
        tempDepart = weatherRow.iloc[0]['depart']
        if tempDepart == 'M':
            tempDepart = 0.0
        # tempFloat = tempDepart.to_float()
        inputData.set_value(index, 'temp depart', tempDepart)

print(inputData)
inputData.to_csv(outputFile)
