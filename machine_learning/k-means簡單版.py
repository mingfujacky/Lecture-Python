import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = np.random.rand(100, 2)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()

clf = KMeans(n_clusters=3)
clf.fit(X)
print(clf.labels_)

plt.scatter(X[:, 0], X[:, 1], c=clf.labels_)
plt.show()