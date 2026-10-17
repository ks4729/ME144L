import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# K1 Testing:
# First data point, 200ml, 15.28s *had vortex
# Second data point, 240ml, 20.07s *had vortex
# Third data point, 345ml, 28.01s *had vortex               -- Was removed
# Fourth data point, 460ml, 23.30s *had small vortex
# Fifth data point, 495ml, 26.92s *had small vortex
# Sixth data point, 560ml, 21.44s *had no vortex
# Seventh data point, 660ml, 26.65s, *had small vortex
# Eighth data point, 660ml, 23.70s, *had small vortex       -- Was removed
# Ninth data point, 475ml, 18.84s
# Tenth data point, 300ml, 15.80s
# Eleventh data point, 200ml, 12.4s *had no vortex
# Twelfth data point, 140ml, 11.15s *had small vortex
# Thirteenth data point, 430ml, 18.8s *had no vortex

# Fourteenth data point, 500ml, 20.02

initial_vol = np.array([200, 240, 460, 495, 560, 660, 475, 300, 200, 140, 430, 500, 500, 500])
time_empty = np.array([15.28, 20.07, 23.30, 26.92, 21.44, 26.65, 18.84, 15.80, 12.4, 11.15, 18.8, 20.02, 20.02, 20.02])

sqrt_initial_vol = np.sqrt(initial_vol)

X = time_empty.reshape(-1, 1)
y = sqrt_initial_vol

# Unconstrained regression
model = LinearRegression(fit_intercept=True).fit(X, y)
Beta = float(model.coef_[0])
Int = float(model.intercept_)
R2 = model.score(X, y)
K = 2 * Beta

# Constrained regression (intercept = 0)
model_zero = LinearRegression(fit_intercept=False).fit(X, y)
Beta_zero = float(model_zero.coef_[0])
R2_zero = model_zero.score(X, y)
K_zero = 2 * Beta_zero

# Print results
print(f"Unconstrained: K1 = {K:.6f}, Intercept = {Int:.6f}, R² = {R2:.4f}")
print(f"Constrained:   K1 = {K_zero:.6f}, R² = {R2_zero:.4f}")

# Plot both regressions
xfit = np.linspace(0, time_empty.max() * 1.1, 200).reshape(-1, 1)

plt.figure(figsize=(8, 5))
plt.scatter(time_empty, y, color='black', label='Experimental Data', zorder=3)

plt.plot(
    xfit, model.predict(xfit),
    label=fr'Unconstrained: $K={K:.4f}$, $R^2={R2:.4f}$'
)

plt.plot(
    xfit, model_zero.predict(xfit),
    linestyle='--',
    label=fr'Constrained: $K={K_zero:.4f}$, $R^2={R2_zero:.4f}$'
)

plt.xlabel(r'$T_e$ (s)')
plt.ylabel(r'$\sqrt{V_0}$ ($\mathrm{cm}^{3/2}$)')
plt.title('Experimental Flow Coefficient Regression')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Results: 
# Unconstrained: K = 1.494054, Intercept = 4.649959, R² = 0.7418
#Constrained:   K = 1.948599, R² = 0.6684




import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# K2 Testing:
# First data point, 155ml, 23.6s *had vortex
# Second data point, 200ml, 21.39s *had no vortex 
# Third data point, 245ml, 32.85s *had vortex
# Fourth data point, 300ml, 38.26s *had vortex
# Fifth data point, 410ml, 35.2s *had no vortex
# Sixth data point, 470ml, 44.56s *had small vortex             *470ml is max volume 

# Seventh data point, 450ml, 37.74s

initial_vol = np.array([155, 200, 245, 300, 470, 450, 450, 450])
time_empty = np.array([23.6, 21.39, 32.85, 38.26, 44.56, 37.74, 37.74, 37.74])

sqrt_initial_vol = np.sqrt(initial_vol)

X = time_empty.reshape(-1, 1)
y = sqrt_initial_vol

# Unconstrained regression
model = LinearRegression(fit_intercept=True).fit(X, y)
Beta = float(model.coef_[0])
Int = float(model.intercept_)
R2 = model.score(X, y)
K = 2 * Beta

# Constrained regression (intercept = 0)
model_zero = LinearRegression(fit_intercept=False).fit(X, y)
Beta_zero = float(model_zero.coef_[0])
R2_zero = model_zero.score(X, y)
K_zero = 2 * Beta_zero

# Print results
print(f"Unconstrained: K2 = {K:.6f}, Intercept = {Int:.6f}, R² = {R2:.4f}")
print(f"Constrained:   K2 = {K_zero:.6f}, R² = {R2_zero:.4f}")

# Plot both regressions
xfit = np.linspace(0, time_empty.max() * 1.1, 200).reshape(-1, 1)

plt.figure(figsize=(8, 5))
plt.scatter(time_empty, y, color='black', label='Experimental Data', zorder=3)

plt.plot(
    xfit, model.predict(xfit),
    label=fr'Unconstrained: $K={K:.4f}$, $R^2={R2:.4f}$'
)

plt.plot(
    xfit, model_zero.predict(xfit),
    linestyle='--',
    label=fr'Constrained: $K={K_zero:.4f}$, $R^2={R2_zero:.4f}$'
)

plt.xlabel(r'$T_e$ (s)')
plt.ylabel(r'$\sqrt{V_0}$ ($\mathrm{cm}^{3/2}$)')
plt.title('Experimental Flow Coefficient Regression')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
