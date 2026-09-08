## LE 1.1: Introduction to Using Python for DSC Lab
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression 

# 1
angle = [-1.57, -1.26, -0.94, -0.63, -0.31, 0., 0.31, 0.65, 0.96, 1.23, 1.52]
voltage = [1.176, 1.648, 1.874, 2.175, 2.438, 2.503, 2.925, 3.067, 3.450, 3.686, 4.014]

x = np.array(voltage).reshape(-1, 1)
y = np.array(angle).reshape(-1, 1)

## Following code is from handout
# Linear Regression
model    = LinearRegression().fit(x, y)
Rsquared = model.score(x, y)
slope, intercept = model.coef_, model.intercept_
print('intercept =', intercept)
print('slope =', slope)
print('coefficient of determination =', Rsquared)

# Plot the raw data and regression using a scatter plot
plt.figure(2)
plt.scatter(x, y, c="r", marker='x')
plt.plot(x,slope*x + intercept)
plt.xlabel('Voltage [Volts]')
plt.ylabel('Angles [Radians]')
plt.legend(['Lin. Reg.','Raw Data'])
plt.title('Regression of Sensor Data')
plt.grid()
plt.show()