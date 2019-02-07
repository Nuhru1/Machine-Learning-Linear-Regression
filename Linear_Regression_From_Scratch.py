import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_data.dropna(inplace=True)
test_data.dropna(inplace=True)

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

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

n = len(x_train)
alpha = 0.0001
epochs = 0

a_0 = np.zeros((n, 1))
a_1 = np.zeros((n, 1))



        

epochs = 0
while(epochs <1000):
    y = a_0 + a_1 * x_train
    error = y - y_train
    mean_sq_er = np.sum(error**2)/n
    
   
    a_0 = a_0 - alpha * 2 * np.sum(error)/n 
    a_1 = a_1 - alpha * 2 * np.sum(error * x_train)/n
    epochs += 1
    
    print(mean_sq_er)
    #f(epochs%10 == 0):
        #print(mean_sq_er)
        

a_0 = a_0[399 : , : ]
a_1= a_1[399 : , : ]


y_prediction = a_0 + a_1 * x_test
print('R2 Score:',r2_score(y_test,y_prediction))

y_plot = []
for i in range(100):
    y_plot.append(a_0[i]+ a_1[i] * i)
plt.figure(figsize=(10,10))
plt.scatter(x_test,y_test,color='red',label='GT')
#lt.plot(range(len(y_plot)),y_plot,color='black',label = 'pred')
plt.plot(y_plot,color='black',label = 'pred')

plt.legend()
plt.show()