# Machine-Learning-Linear-Regression

Simple linear regression is a type of regression analysis where the number of independent variables is one and there is a linear relationship between the independent(x) and dependent(y) variable. Based on the given data points, we try to plot the best fit straight line that model all the points the best.

 The line can be modelled based on the linear equation :
y = a_0 + a_1 * x

The motive of the linear regression algorithm is to find the best values for a_0 and a_1. For that we will use the cost function.

## Cost Function

Since we want the best values for a_0 and a_1, we convert this search problem into a minimization problem where we would like to minimize the error between the predicted value and the actual value.

![lr](https://user-images.githubusercontent.com/44145876/52446701-b9c88f00-2b69-11e9-8f15-b3fbe162e1b4.png)

The difference between the predicted values and ground truth measures the error difference. We square the error difference and sum over all data points and divide that value by the total number of data points. This provides the average squared error over all the data points.Therefore, this cost function is also known as the Mean Squared Error(MSE) function. Now, using this MSE function we are going to change the values of a_0 and a_1 such that the MSE value settles at the minima. For that we will the gradient descent.

# Gradient descent

 Gradient descent is a method of updating a_0 and a_1 to reduce the cost function(MSE). The idea is that we start with some values for a_0 and a_1 and then we change these values iteratively to reduce the cost. 

![gd](https://user-images.githubusercontent.com/44145876/52447095-c13c6800-2b6a-11e9-8026-3af987f13b85.png)

The partial derivates are the gradients and they are used to update the values of a_0 and a_1. Alpha is the learning rate which is a hyperparameter that you must specify. A smaller learning rate could get you closer to the minima but takes more time to reach the minima, a larger learning rate converges sooner but there is a chance that you could overshoot the minima.
