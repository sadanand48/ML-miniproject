import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('brain_head.csv')
print(data.head())
print(data.describe())

X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values

mean_x=np.mean(X)
mean_y=np.mean(Y)

n=len(X)

a=0
b=0

for i in range(n):
	a+=(X[i]-mean_x)*(Y[i]-mean_y)
	b+=(X[i]-mean_x)**2

b1=a/b
b0=mean_y -(b1*mean_x)

print(b1,b0)
#the predicted line will be y=b0 + b1*x

print("Predicted regression line: y=" + str(b0) + str(b1)+"x")

x_max = np.max(X) + 100
x_min = np.min(X) - 100

#calculating line values of x and y
x = np.linspace(x_min, x_max, 1000)
y = b0 + b1 * x

#plotting line 
plt.plot(x, y, color='#00ff00', label='Linear Regression')

#plot the data point
plt.scatter(X, Y, color='#ff0000', label='Data Point')

# x-axis label
plt.xlabel('Head Size (cm^3)')

#y-axis label
plt.ylabel('Brain Weight (grams)')


rmse = 0
for i in range(n):
    y_pred=  b0 + b1* X[i]
    rmse += (Y[i] - y_pred) ** 2
    
rmse = np.sqrt(rmse/n)

print(rmse)

sumofsquares = 0
sumofresiduals = 0

for i in range(n) :
    y_pred = b0 + b1 * X[i]
    sumofsquares += (Y[i] - mean_y) ** 2
    sumofresiduals += (Y[i] - y_pred) **2
    
score  = 1 - (sumofresiduals/sumofsquares)

print(score)
plt.legend()
plt.show()
