# Find out the non-zero store-item combination and label as 1 otherwise 0;

import pandas as pd

testFile = "Data/test.csv"
trainFile = "Data/train.csv"
outputFile = "Data/testProcessed_0.csv"

trainData = pd.read_csv(trainFile)
testData = pd.read_csv(testFile)

g = trainData.groupby(["store_nbr", "item_nbr"])['units'].mean()
g = g[g > 0]

store_nbrs = g.index.get_level_values(0)
item_nbrs = g.index.get_level_values(1)

testData.insert(3, 'units', 0)
lens = len(store_nbrs)
# print(testData)

for index, row in testData.iterrows():
    # print(str(store_nbrs[i]) + " : " + str(item_nbrs[i]))
    tempStoreNum = row['store_nbr']
    tempItemNum = row['item_nbr']
    for i in range(lens):
        if store_nbrs[i]==tempStoreNum and item_nbrs[i]==tempItemNum:
            testData.set_value(index, 'units', 1)

# print(testData)
testData.to_csv(outputFile)



