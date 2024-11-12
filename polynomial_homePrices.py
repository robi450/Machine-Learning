import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Historical Data and Estimation Parameters
years = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 0 is the current year, to 10 years in the future

# Home Price Growth (Approximate historical trend)
home_prices = np.array([209000, 224000, 240000, 260000, 274000, 300000, 325000, 350000, 380000, 385833, 401000])

# Median Rent (with a slight decline)
initial_rent = 2041
rental_prices = initial_rent * (1 - 0.01) ** years  # Assuming a slight 1% annual decrease in rent

# Polynomial Regression for Home Prices
poly_features = PolynomialFeatures(degree=2)  # Fit with a quadratic polynomial
years_poly = poly_features.fit_transform(years.reshape(-1, 1))

home_model = LinearRegression()
home_model.fit(years_poly, home_prices)

future_years = np.linspace(0, 10, 100).reshape(-1, 1)  # More detailed points for the next 10 years
future_years_poly = poly_features.transform(future_years)
predicted_home_prices = home_model.predict(future_years_poly)

# Plot Home Prices
plt.figure(figsize=(12, 6))
plt.plot(future_years, predicted_home_prices, label='Predicted Home Prices', color='blue')
plt.scatter(years, home_prices, color='blue', marker='o', label='Actual Home Prices')

# Polynomial Regression for Rental Prices
rent_model = LinearRegression()
rent_model.fit(years_poly, rental_prices)

predicted_rental_prices = rent_model.predict(future_years_poly)

# Plot Rental Prices
plt.plot(future_years, predicted_rental_prices * 12, label='Predicted Yearly Rent', color='red')
plt.scatter(years, rental_prices * 12, color='red', marker='x', label='Actual Yearly Rent')

plt.xlabel('Years from Now')
plt.ylabel('Cost ($)')
plt.title('Home Prices vs Yearly Rental Costs in Tampa Bay Area (Next 10 Years)')
plt.legend()
plt.grid(True)
plt.show()

# Cumulative Cost Analysis over 10 Years
cumulative_home_cost = sum(predicted_home_prices)  # Total home cost over 10 years
cumulative_rent_cost = sum(predicted_rental_prices) * 12  # Total rent cost over 10 years

print(f"Cumulative cost of buying over 10 years: ${cumulative_home_cost:.2f}")
print(f"Cumulative cost of renting over 10 years: ${cumulative_rent_cost:.2f}")

