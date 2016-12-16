import pandas as pd

inputFile = 'Data/submit_knn_21.csv'
outputFile = 'Data/submit_knn_21.csv'

inputData = pd.read_csv(inputFile)
# inputData = inputData.drop('Unnamed: 0', 1)
inputData.insert(0, 'id', 0)

inputData['id'] = inputData['store_nbr'].map(str) + '_' + inputData['item_nbr'].map(str) + '_' + inputData['date']

# print(inputData)
inputData.to_csv(outputFile, index=False, columns=['id', 'units'])
