import numpy as np
import pandas as pd
PlayTennis = pd.read_csv("./Datasets/Play tennis.csv")
from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()

PlayTennis['Outlook'] = Le.fit_transform(PlayTennis['Outlook'])
PlayTennis['Temperature'] = Le.fit_transform(PlayTennis['Temperature'])
PlayTennis['Humidity'] = Le.fit_transform(PlayTennis['Humidity'])
PlayTennis['Windy'] = Le.fit_transform(PlayTennis['Windy'])
y = PlayTennis['PlayTennis']
x = PlayTennis.drop(['PlayTennis'], axis = 1)
from sklearn import tree
classifier = tree.DecisionTreeClassifier(criterion = 'entropy')
classifier = classifier.fit(x, y)
tree.plot_tree(classifier) 

X_pred = classifier.predict(x)
X_pred == y