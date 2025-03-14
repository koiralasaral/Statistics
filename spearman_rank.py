import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Generate random data
ages = np.random.randint(18, 80, 100)
accidents = np.random.poisson(lam=(80 - ages) / 10, size=100)

# Calculate the Spearman rank correlation coefficient
spearman_corr, _ = spearmanr(ages, accidents)

# Plot the data
plt.scatter(ages, accidents)
plt.title(f"Spearman Rank Correlation: {spearman_corr:.2f}")
plt.xlabel("Age of Driver")
plt.ylabel("Number of Accidents")
plt.show()

# Create a bivariate frequency distribution
age_bins = np.arange(18, 81, 5)
accident_bins = np.arange(0, max(accidents) + 1, 1)
frequency_distribution, age_edges, accident_edges = np.histogram2d(ages, accidents, bins=[age_bins, accident_bins])

# Plot the bivariate frequency distribution (heatmap)
plt.imshow(frequency_distribution.T, origin='lower', aspect='auto', interpolation='nearest', cmap='Blues',
           extent=[age_edges[0], age_edges[-1], accident_edges[0], accident_edges[-1]])
plt.colorbar(label='Frequency')
plt.title('Bivariate Frequency Distribution of Age and Accidents')
plt.xlabel('Age of Driver')
plt.ylabel('Number of Accidents')
plt.show()
