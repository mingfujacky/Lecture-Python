import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC

iris = load_iris()
# print(iris.DESCR)
X = iris.data
Y = iris.target
X = X[:, :2]
x_train, x_test, y_train, y_test = train_test_split(X, Y,      
                                     test_size=0.2, random_state=87)
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap = 'viridis')
plt.show()
 
clf = SVC()
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)
plt.scatter(x_test[:, 0], x_test[:, 1], c = y_predict, cmap = 'viridis')
plt.show()
 
difference = y_predict - y_test #預測答案減掉正確答案
plt.scatter(x_test[:, 0], x_test[:, 1], c = difference, cmap = 'plasma')
plt.show()

# use numpy meshgrid
x = np.arange(4, 8, 0.02)
y = np.arange(2, 5, 0.02)
xc, yc = np.meshgrid(x, y)

plt.scatter(xc, yc)
plt.show()

# 把 grid的數據送進去分類器預測
xc = xc.ravel()
yc = yc.ravel()
mesh_X = list(zip(xc, yc))
mesh_predicted_Y = clf.predict(mesh_X)
plt.scatter(xc, yc, c=mesh_predicted_Y)
plt.show()



