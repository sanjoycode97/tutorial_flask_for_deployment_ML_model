import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib



url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"


column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# read the url
df = pd.read_csv(url)

X = df.iloc[:,0:8]
y = df.iloc[:,8]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

#train the model
model = LogisticRegression()
model.fit(X_train, y_train)
print("[INFO] model trained")

#accuracy
result = model.score(X_test, y_test)
print(f"[INFO] - accuracy is {result}")

#save the model
joblib.dump(model, "saved_logitic_model.pkl")