import pandas as pd

inputFile = 'Data/dataWithWeather.csv'
outputFile = 'Data/finalTrain_0.csv'

inputData = pd.read_csv(inputFile)
inputData.drop('Unnamed: 0', 1)
inputData.insert(3, 'isWeekend', 0)

for index, row in inputData.iterrows():
    weekday = row['weekday']
    if weekday == 5 or weekday == 6:
        inputData.set_value(index, 'isWeekend', 1)

# print(inputData)
inputData.to_csv(outputFile)