import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
data = pd.read_csv("./Datasets/Play tennis.csv")
print(f"The first 5 data of training input: \n {data.head()}")
X = data.iloc[:, :-1]
print (f"The first 5 values of train data: \n{X.head()}")
Y = data.iloc[:, -1]
print(f"The first 5 values of train data: \n{Y.head()}")
leOutlook, leTemperature, leHumidity, leWindy = LabelEncoder(), LabelEncoder(), LabelEncoder(), LabelEncoder()

X.Outlook = leOutlook.fit_transform(X.Outlook)
X.Temperature = leTemperature.fit_transform(X.Temperature)
X.Humidity = leHumidity.fit_transform(X.Humidity)
X.Windy = leWindy.fit_transform(X.Windy)
print(f"Now the trained data is: \n{X.head()}")
lePlayTennis = LabelEncoder()
Y.PlayTennis = lePlayTennis.fit_transform(Y)
print(f"Now the Test Data is: \n{Y}")
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)
classifier = GaussianNB()
classifier.fit(x_train, y_train)
from sklearn.metrics import accuracy_score
print(f"Accuracy: {accuracy_score(classifier.predict(x_test), y_test)}")