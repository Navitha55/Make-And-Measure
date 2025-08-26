import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('C:/Users/navit/projects/demo/synthetic_stitching_data.csv')

X = df.drop(columns=['stitching_cost'])
y = df['stitching_cost']

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open('stitching_model.pkl', 'wb') as f:
    pickle.dump(model, f)

