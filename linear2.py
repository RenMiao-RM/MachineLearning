import pandas as pd
from sklearn import linear_model
import numpy as np
import math

testFile = 'Data/testProcessed_4.csv'
trainFile = 'Data/finalTrain_1.csv'
outputFile = 'Data/submit_ridge_1000.csv'

testData = pd.read_csv(testFile)
testData.insert(1, 'log1p', 0)

testData['log1p'] = np.log(testData['units'] + 1)

trainData = pd.read_csv(trainFile)
trainData.insert(1, 'log1p', 0)
trainData['log1p'] = np.log(trainData['units'] + 1)

trainData.insert(1, 'days', 0)
testData.insert(1, 'days', 0)

testData['days'] = (pd.to_datetime(testData['date']) - pd.to_datetime('2012/1/1')).dt.days
trainData['days'] = (pd.to_datetime(trainData['date']) - pd.to_datetime('2012/1/1')).dt.days

# print(trainData)

dict = {}
# feature_cols = ['temp depart', 'weekday', 'isWeekend', 'isHoliday', 'days', 'SnowFall', 'PrecipTotal', 'aveWindSpeed']
feature_cols = ['temp depart', 'weekday', 'isWeekend', 'isHoliday', 'days']
label_col = ['log1p']
# label_col = ['units']

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
        y = trainRows[label_col]
        # linreg = linear_model.Lasso(alpha=0.5)
        linreg = linear_model.Ridge(alpha=1000)
        linreg.fit(x, y)
        trainModel = linreg
        dict[tuple] = trainModel
    # print(trainRows)

    x_test = pd.DataFrame(row[feature_cols])
    # print(x_test)
    x_test = x_test.transpose()
    # print(x_test)
    # try:
    y_pred = trainModel.predict(x_test)
    if y_pred < 0:
        y_pred = 0
    # except Exception,ex:
    #   print sno,ino
    # df_test['log1p'] = y_pred
    # df_test['units'] = np.exp(y_pred)-1
    # df_test.to_csv('model/result/df_result_'+str(sno)+'_'+str(ino)+'.csv')
    testData.set_value(index, 'units', int(math.exp(y_pred)-1))
    # testData.set_value(index, 'units', y_pred)

# print(testData)
# testData.to_csv(outputFile)
testData.insert(0, 'id', 0)

testData['id'] = testData['store_nbr'].map(str) + '_' + testData['item_nbr'].map(str) + '_' + testData['date']

testData.to_csv(outputFile, index=False, columns=['id', 'units'])