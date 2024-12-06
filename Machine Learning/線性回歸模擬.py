import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# #根據 y = 1.2x + 0.8 產生一組數據
# x = np.linspace(0, 5, 50)
# y = 1.2 * x + 0.8
# plt.scatter(x, y)
# plt.show()

# # 增加雜訊 y = 1.2x + 0.8 + 雜訊
# x = np.linspace(0, 5, 50)
# y = 1.2 * x + 0.8 + 0.5 * np.random.randn(50)
# plt.scatter(x, y)
# plt.show()

# # 畫在一起
# x = np.linspace(0, 5, 50)
# y = 1.2 * x + 0.8 + 0.5 * np.random.randn(50)
# plt.scatter(x, y)
# plt.plot(x, 1.2 * x + 0.8, 'b')
# plt.show()

# 使用sklearn幫我們找線性回歸線
x = np.linspace(0, 5, 50)
y = 1.2 * x + 0.8 + 0.5 * np.random.randn(50)

regr = LinearRegression()
X = x.reshape(len(x), 1)
regr.fit(X, y)
print(regr.predict([[1.3],[2.0]])) # need 2D array as parameter
print(regr.predict([[0.5],])) # need 2D array as parameter
print(regr.predict([[0.1]])) # need 2D array as parameter

Y = regr.predict(X)
plt.scatter(x, y)
plt.plot(x, Y, 'r')
plt.plot(x, 1.2 * x + 0.8, 'b')
plt.show()
