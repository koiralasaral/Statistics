import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Generate some example data
np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)

# Create a DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# Plot the bivariate frequency distribution
plt.figure(figsize=(10, 6))
sns.histplot(data, x='x', y='y', bins=30, cbar=True)

plt.title('Bivariate Frequency Distribution')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
# Generate some example data for positive correlation
np.random.seed(0)
age = np.random.randint(18, 80, 1000)
accidents = age * 0.1 + np.random.randn(1000) * 5

# Create a DataFrame
data = pd.DataFrame({'age': age, 'accidents': accidents})

# Plot the bivariate frequency distribution
plt.figure(figsize=(10, 6))
sns.histplot(data, x='age', y='accidents', bins=30, cbar=True)

plt.title('Positive Correlation between Age of Driver and Number of Accidents')
plt.xlabel('Age of Driver')
plt.ylabel('Number of Accidents')
plt.show()