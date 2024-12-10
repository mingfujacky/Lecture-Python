import numpy as np
import matplotlib.pyplot as plt 
from sklearn.svm import SVC

# X, Y 拿來建模的數據
X = np.array([[-3, 2], [-6, 5], [3, -4], [2, -8]])
Y = np.array([1, 1, 2, 2])
plt.scatter(X[:,0], X[:,1], c = Y, cmap = 'Paired')
plt.show()

# 訓練一個分類器
clf = SVC(gamma='auto')
clf.fit(X, Y)

# 產生一組 -6 < x < 3 和 -8 < y < 5 的grid的數據
x_min, x_max, y_min, y_max = (-6, 3, -8, 5)
xx = np.linspace(x_min, x_max, x_max-x_min+1)
yy = np.linspace(y_min, y_max, y_max-y_min+1)
xc, yc = np.meshgrid(xx, yy)
plt.scatter(xc, yc)
plt.show()

# 把 grid的數據送進去分類器預測
xc = xc.ravel()
yc = yc.ravel()
mesh_X = list(zip(xc, yc))
mesh_predicted_Y = clf.predict(mesh_X)
plt.scatter(xc, yc, c=mesh_predicted_Y)
plt.show()
