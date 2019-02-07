import pandas as pd
import numpy as np

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_data.dropna(inplace=True)


x_train = train_data['x']
y_train = train_data['y']

x_test = test_data['x']
y_test = test_data['y']

x_train = np.array(x_train)
y_train = np.array(y_train)

x_test = np.array(x_test)
y_test = np.array(y_test)

x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression(normalize=True)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(r2_score(y_test, y_pred))