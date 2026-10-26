import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


displacement = np.array([0.9, 0.4, -0.8, -1.6])
force = np.array([1, 0.5, -0.5, -1])

X = displacement.reshape(-1, 1)
Y = force.reshape(-1, 1)

# Unconstrained regression
model = LinearRegression(fit_intercept=True).fit(X, Y)
R2 = model.score(X, Y)

inputSpace = np.linspace(displacement.min()*1.1, displacement.max() * 1.1, 200).reshape(-1, 1)
theoreticalK = 85e-2 #N/m

plt.figure(figsize=(8, 5))
plt.scatter(displacement, force, label='Experimental Data')
plt.plot(inputSpace, model.predict(inputSpace), label=fr'Linear Regression Fit, $R^2={R2:.4f}$')
plt.plot(inputSpace, theoreticalK*inputSpace, label=fr'Theoretical Slope')

plt.xlabel("Displacement (cm)")
plt.ylabel("Force (N)")
plt.title('Fit for ')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

print(f"Theoretical Slope is {theoreticalK}")
print(f"Fit Slope is {model.coef_[0]}")

# slope for upper stage seems to be 1N/cm (all our measurements were exactly on)
# slope for lower stage seems to be 0.8N/cm (experimentally derived)
# mass per stage seems to be 649.3g

