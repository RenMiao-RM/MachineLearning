import pandas as pd
from sklearn import linear_model

testFile = 'Data/testProcessed_3.csv'
trainFile = 'Data/finalTrain_1.csv'
outputFile = 'Data/submit_ridge_0.5.csv'

testData = pd.read_csv(testFile)
trainData = pd.read_csv(trainFile)
# trainData = trainData.drop('Unnamed: 0', 1)
# trainData = trainData.drop('Unnamed: 0.1', 1)

# testData = testData.drop('Unnamed: 0', 1)
# testData = testData.drop('Unnamed: 0.1', 1)

# print(testData)
dict = {}
feature_cols = ['temp depart', 'isWeekend', 'isHoliday', 'SnowFall', 'PrecipTotal']
lable_col = ['units']

for index, row in testData.iterrows():
    # if sno == 35:
    #     continue
    if (int) (row['units']) == 0:
        continue

    storeNum = row['store_nbr']
    itemNum = row['item_nbr']
    tuple = (storeNum, itemNum)
    if tuple in dict:
        trainModel = dict.get(tuple)
    else:
        trainRows = trainData[(trainData['store_nbr'] == storeNum) & (trainData['item_nbr'] == itemNum)]
        x = trainRows[feature_cols]
        y = trainRows[lable_col]
        linreg = linear_model.Ridge(alpha=0.5)
        linreg.fit(x, y)
        trainModel = linreg
        dict[tuple] = trainModel
    # print(trainRows)

    x_test = pd.DataFrame(row[feature_cols]).transpose()
    # try:
    y_pred = trainModel.predict(x_test)
    # except Exception,ex:
    #   print sno,ino
    # df_test['log1p'] = y_pred
    # df_test['units'] = np.exp(y_pred)-1
    # df_test.to_csv('model/result/df_result_'+str(sno)+'_'+str(ino)+'.csv')
    testData.set_value(index, 'units', y_pred)

# print(testData)
# testData.to_csv(outputFile)
testData.insert(0, 'id', 0)

testData['id'] = testData['store_nbr'].map(str) + '_' + testData['item_nbr'].map(str) + '_' + testData['date']

testData.to_csv(outputFile, index=False, columns=['id', 'units'])