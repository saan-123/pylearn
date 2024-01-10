from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
iris = datasets.load_iris()
print(iris)
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target)
model = KMeans(n_clusters = 3)
model.fit(X_train, Y_train)
model.score
print(f"K-Means: {metrics.accuracy_score(Y_test, model.predict(X_test))}")
from sklearn.mixture import GaussianMixture
model2 = GaussianMixture (n_components = 4)
model2.fit(X_train, Y_train)
model2.score
print(f"EM Algorithm: {metrics.accuracy_score(Y_test, model2.predict(X_test))}")


# To Plot the Graph
"""
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./Datasets/7.csv")

x1 = data['x'].values
x2 = data['y'].values

X = np.asarray(list(zip(x1, x2))) # Convert to numpy array
plt.scatter(x1, x2)
plt.show()

markers = ['s', 'o', 'v']
k = 3
clusters = KMeans(n_clusters=k).fit(X)
for i, l in enumerate(clusters.labels_):
    plt.plot(x1[i], x2[i], marker=markers[l])
plt.tight_layout()
plt.show()
"""