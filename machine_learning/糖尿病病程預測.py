import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

diabetes = load_diabetes(return_X_y=False)    
# print(diabetes.DESCR)
print("feature names:", diabetes.feature_names)
print("data shape: ", diabetes.data.shape)
print("target shape: ", diabetes.target.shape)

# 把「給模型當作參考的特徵」叫做 X， 「要模型去學的答案」叫做 Y
X = diabetes.data
Y = diabetes.target
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

# 叫出函數學習機 --> 訓練函數學習機 --> 把函數學習機拿來用
regr = LinearRegression()
regr.fit(x_train, y_train)
y_predict = regr.predict(x_test)

# 真實的結果(y_test)當作 x 座標， 預測的結果(y_predict)當作 y 座標描點在圖上
plt.rcParams['font.sans-serif']=['Heiti TC']
plt.scatter(y_test, y_predict)
plt.plot([0, 300], [0, 300], 'r')
plt.xlabel('真實的結果')
plt.ylabel('預測的結果')
plt.show()