import pandas as pd

inputFile = 'Data/dataWithStation.csv'
weatherFile = 'Data/weather.csv'
outputFile = 'Data/dataWithWeather.csv'

inputData = pd.read_csv(inputFile)

# print(inputData)
weatherData = pd.read_csv(weatherFile)
inputData = inputData.drop('Unnamed: 0', 1)
inputData = inputData.drop('Unnamed: 0.1', 1)

inputData.insert(1, 'temp depart', 0)
# print(inputData)

for index, row in inputData.iterrows():
    # find the station # according to the store #
    stationNum = row['station_nbr']
    dateInfo = row['date']
    # print(stationNum)

    weatherRow = weatherData[(weatherData['station_nbr'] == stationNum) & (weatherData['date'] == dateInfo)]
    tempDepart = weatherRow.iloc[0]['depart']
    if (tempDepart == 'M'):
        tempDepart = 0.0
    # tempFloat = tempDepart.to_float()
    inputData.set_value(index, 'temp depart', tempDepart)

inputData.to_csv(outputFile)
