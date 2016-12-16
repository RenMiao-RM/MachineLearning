import pandas as pd

trainFile = "Data/train.csv"
testFile = "Data/train.csv"
trainFileNoZero = "Data/trainNoZero.csv"

trainData = pd.read_csv(trainFile)
# testData = pd.read_csv(testFile)
print(trainData)

g = trainData.groupby(["store_nbr", "item_nbr"])['units'].mean()
g = g[g > 0]

# print(g)

store_nbrs = g.index.get_level_values(0)
item_nbrs = g.index.get_level_values(1)

# print(store_nbrs)
# print(item_nbrs)

lens = len(store_nbrs)
# columns = ['date', 'store_nbr', 'item_nbr', 'units']
# trainDataNoZero = pd.DataFrame(index=[], columns=['date', 'store_nbr', 'item_nbr', 'units'])
trainDataNoZero = None
for i in range(0, lens):
    # print(str(store_nbrs[i]) + " : " + str(item_nbrs[i]))
    tempStoreNum = store_nbrs[i]
    tempItemNum = item_nbrs[i]
    tempRow = trainData[(trainData['store_nbr'] == tempStoreNum) & (trainData['item_nbr'] == tempItemNum)]
    if trainDataNoZero is None:
        trainDataNoZero = pd.DataFrame(tempRow)
    else:
        trainDataNoZero = trainDataNoZero.append(tempRow)

print(trainDataNoZero)
# trainDataNoZero.to_csv(trainFileNoZero)



