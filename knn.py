#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
import pandas as pd
testFile = 'Data/testProcessed_3.csv'
trainFile = 'Data/finalTrain_1.csv'
outputFile = 'Data/submit_knn_21.csv'

testData = pd.read_csv(testFile)
testData['days'] = (pd.to_datetime(testData['date']) - pd.to_datetime('2012/3/17')).dt.days
trainData = pd.read_csv(trainFile)
trainData['days'] = (pd.to_datetime(trainData['date']) - pd.to_datetime('2012/3/17')).dt.days

dict = {}
for index, row in testData.iterrows():
    # if sno == 35:
    #     continue
    if (int) (row['units']) == 0:
        continue

    storeNum = row['store_nbr']
    itemNum = row['item_nbr']
    tuple = (storeNum, itemNum)
    if tuple in dict:
        trainRows = dict.get(tuple)
    else:
        trainRows = trainData[(trainData['store_nbr'] == storeNum) & (trainData['item_nbr'] == itemNum)]
        dict[tuple] = trainRows
    # print(trainRows)
    knn = neighbors.KNeighborsRegressor(n_neighbors=21)
    feature_cols = ['days']
    trainRows['log1p'] = np.log(trainRows['units'] + 1)
    lable_col = ['log1p']
    x = trainRows[feature_cols]
    y = trainRows[lable_col]
    knn.fit(x, y)
    x_test = pd.DataFrame(row[feature_cols]).transpose()
    # try:
    y_pred = knn.predict(x_test)
    # except Exception,ex:
    #   print sno,ino
    y_pred_1=np.rint(np.exp(y_pred)-1)
    # df_test['units'] = np.exp(y_pred)-1
    # df_test.to_csv('model/result/df_result_'+str(sno)+'_'+str(ino)+'.csv')
    testData.set_value(index, 'units', y_pred_1)

'''
trainData2 = trainData[trainData['units']>0]
knn = neighbors.KNeighborsRegressor()
feature_cols = ['isWeekend', 'isHoliday','PrecipTotal','store_nbr','item_nbr']
trainData2['log1p'] = np.log(trainData2['units'] + 1)
lable_col = ['log1p']
x = trainData2[feature_cols]
y = trainData2[lable_col]
knn.fit(x, y)
x_test = testData[feature_cols]
# try:
y_pred = knn.predict(x_test)
# except Exception,ex:
#   print sno,ino
testData['log1p'] = y_pred
testData['units'] = np.rint(np.exp(y_pred)-1)
# df_test.to_csv('model/result/df_result_'+str(sno)+'_'+str(ino)+'.csv')
#testData['units']=y_pred
'''
print(testData)
testData.to_csv(outputFile, index=False)

