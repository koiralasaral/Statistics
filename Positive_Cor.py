import numpy as np
import matplotlib.pyplot as plt

# Generate some data
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient}")

# Plot the data
plt.scatter(x, y)
plt.title(f"Scatter plot with positive correlation (r = {correlation_coefficient:.2f})")
plt.xlabel("X")
plt.ylabel("Y")
# Show the plot
plt.show()

# Additional code to analyze the relationship between age of driver and number of accidents
# Generate some example data
np.random.seed(0)
ages = np.random.randint(18, 80, 100)
accidents = np.random.poisson(lam=(80 - ages) / 10, size=100)

# Calculate the correlation coefficient
correlation_coefficient_age_accidents = np.corrcoef(ages, accidents)[0, 1]
print(f"Correlation Coefficient between age and number of accidents: {correlation_coefficient_age_accidents}")

# Plot the data
plt.scatter(ages, accidents)
plt.title(f"Scatter plot of age vs number of accidents (r = {correlation_coefficient_age_accidents:.2f})")
plt.xlabel("Age of Driver")
plt.ylabel("Number of Accidents")
plt.show()

# Create a bivariate frequency distribution
age_bins = np.arange(18, 81, 5)
accident_bins = np.arange(0, max(accidents) + 1, 1)
frequency_distribution, age_edges, accident_edges = np.histogram2d(ages, accidents, bins=[age_bins, accident_bins])

# Print the bivariate frequency distribution
print("Bivariate Frequency Distribution (Age vs Number of Accidents):")
print(frequency_distribution)