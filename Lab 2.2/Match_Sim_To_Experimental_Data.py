#
# Match Compound Pend Sim to Experimental Data
# ER Fall '26
# 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.close('all') # close all plots

# --------------------------------------
# Fixed-step RK4 integrator
# --------------------------------------
def rk4fixed(f, x0, t, args=()):
    x = np.zeros((len(t), len(x0)))
    x[0] = x0

    for i in range(len(t) - 1):
        h = t[i+1] - t[i]

        k1, _ = f(x[i], t[i], *args)
        k2, _ = f(x[i] + 0.5*h*k1, t[i] + 0.5*h, *args)
        k3, _ = f(x[i] + 0.5*h*k2, t[i] + 0.5*h, *args)
        k4, _ = f(x[i] + h*k3, t[i] + h, *args)

        x[i+1] = x[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    return x

# --------------------------------------
# Experimental Data
# --------------------------------------
fileName = "test1.csv" # set to your specific filename

# Read csv file
data = pd.read_csv(fileName)

# Extract data from dataframe
t = np.array(data.Time)
v = np.array(data.voltage)

# Set T1 and T2 to plot data over times of interest
# Plot all data: 
T1,T2 = 2.867, t[-1]

# or choose specific endpoints as below:
# T1 = 1.81
# T2 = T1 + 10


# the next lines determine the index values for your specified times
it1 = np.nonzero(t > T1)[0][0]
it2 = np.nonzero(t < T2)[0][-1]

# create new arrays for values between T1 and T2
T = t[it1:it2] - t[it1] # Resets initial time to zero seconds
V = v[it1:it2]

# --------------------------------------
# Utilize Calibration to Convert to Angular Displacement
# --------------------------------------

# --- Write down calibration values ---
Slope      = 64.28       # NOTE: Replace with calibration value
Intercept  = -211.92     # NOTE: Replace with calibration value
theta_meas = Slope * V + Intercept


# --------------------------------------
# Run Simulation per Experimental Time and x0
# --------------------------------------

# Python indices start at 0
# x = [x1, x2]
# where x1 = x[0], and x2 = x[1]

# define the system ODEs
def pendulum(x, t, m, g, Lc, b, Jo, To):
    x1 = x[0]
    x2 = x[1]
    xdot1 = x2
    xdot2 = (1/Jo)*(-b*x2 - To*np.sign(x2) - m*g*Lc*np.sin(x1))
    # specify outputs
    y = 0
    
    return np.array([xdot1, xdot2]), y

m  = 0.187        # kg
g  = 9.81         # m/s²
Lc = 0.1987              # Center of gravity location from pivot (m)
Jo = 1*0.00843            # Moment of inertia about pivot (kg·m²)
b  = 1*0.0     # Linear/Viscous damping coefficient (N·m·s/rad)
To = 1*0.00872           # Nonlinear/Coulomb friction torque (N·m)

# initially deflect and release mass from rest
# x0 = [x10, x20] where x0 = x at time t=0
Rad2Deg = 180/np.pi # Conversion rate for Radians to Degrees
x0 = np.array([-90/Rad2Deg, 0.0]) # Sim ICs need to be in [rad] and [rad/s] units

t = T # Match to time array from Measured Data
sol = rk4fixed(pendulum, x0, t, args=(m, g, Lc, b, Jo, To))

# Pull angular displacement [rad] values from the "Sol" output
Theta = sol[:,0] # rad
Omega = sol[:,1] # rad/s


plt.plot(t, Theta*Rad2Deg, label='Pend Sim')
plt.plot(T, theta_meas, color='r', linestyle='--', label = "Experimental Data")
plt.xlabel('Time [s]')
plt.ylabel('Angular Displacement [deg]')
plt.legend()
plt.xlim(0, t[-1])
plt.ylim(-100, 100)
plt.grid()
plt.show()

