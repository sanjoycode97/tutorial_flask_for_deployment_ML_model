import joblib

model=joblib.load("saved_logitic_model.pkl")

print(model.predict([[1,1,1,1,1,1,1,1]]))