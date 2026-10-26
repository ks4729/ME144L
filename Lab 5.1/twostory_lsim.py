# two story model
# ME 144L Spring 2022

import math
import numpy as np
from numpy.linalg import eig
from scipy.signal import lsim, lti
import matplotlib.pyplot as plt

# Sample values
m1 = 0.65
m2 = 0.65
k1 = 159
k2 = 159
b1 = 0.001
b2 = 0.001

amat = np.array([[0,1,0,0],[-k1/m1,-(b1+b2)/m1,k2/m1,b2/m1],
                 [0,-1,0,1],[0,b2/m2,-k2/m2,-b2/m2]])

bmat = np.array([[0],[0],[0],[0]])

# displacements as outputs
cmat = np.array([[1,0,0,0],[0,0,1,0]])

dmat = np.array([[0],[0]])

# linear simulation

sys = lti(amat,bmat,cmat,dmat)

t = np.linspace(0,5, num = 500)
u = np.zeros_like(t)
x0 = np.array([0.025, 0.0, 0.030, 0.0])

tout, y, x = lsim(sys, u, t, x0)

plt.plot(tout, y[:, 0], label='Mass 1')
plt.plot(tout, y[:, 1], label='Mass 2')
plt.title("Displacement vs Time")
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.show()


# accelerations as outputs
cmat = np.array([amat[1], amat[1] + amat[3]]) # Mass 2 absolute acceleration

# linear simulation

sys = lti(amat, bmat, cmat, dmat)

tout, y, x = lsim(sys, u, t, x0)

plt.plot(tout, y[:, 0], label='Mass 1')
plt.plot(tout, y[:, 1], label='Mass 2')
plt.title("Acceleration vs Time")
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.legend()
plt.show()