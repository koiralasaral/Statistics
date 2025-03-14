import numpy as np
from scipy.stats import rankdata
import matplotlib.pyplot as plt 
def spearman_rank_correlation(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Both arrays must have the same length")
    
    rank_x = rankdata(x)
    rank_y = rankdata(y)
    
    d = rank_x - rank_y
    d_squared = d ** 2
    
    numerator = 6 * np.sum(d_squared)
    denominator = n * (n**2 - 1)
    
    return 1 - (numerator / denominator)

# Example usage
x = [10, 20, 20, 40, 50]
y = [30, 10, 20, 40, 50]
print(spearman_rank_correlation(x, y))

# Plot the data 
plt.scatter(x, y)
plt.title(f"Spearman Rank Correlation: {spearman_rank_correlation(x, y):.2f}")  
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
# Additional code to analyze the relationship between age of driver and number of accidents
# Generate some example data        
np.random.seed(0)
ages = np.random.randint(18, 80, 100)
accidents = np.random.poisson(lam=(80 - ages) / 10, size=100)

# Calculate the Spearman rank correlation coefficient
spearman_corr = spearman_rank_correlation(ages, accidents)              

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

# Print the bivariate frequency distribution
print("Bivariate Frequency Distribution (Age vs Number of Accidents):")
print(frequency_distribution)
# Plot the bivariate frequency distribution (heatmap)
plt.imshow(frequency_distribution.T, origin='lower', aspect='auto', interpolation='nearest', cmap='viridis',
           extent=[age_edges[0], age_edges[-1], accident_edges[0], accident_edges[-1]])
plt.colorbar(label='Frequency')
plt.title('Bivariate Frequency Distribution of Age and Accidents')
plt.xlabel('Age of Driver')
plt.ylabel('Number of Accidents')
plt.show()
# Output:
# 0.1
# 0.1
# Bivariate Frequency Distribution (Age vs Number of Accidents):
# [[
#
#
#
#
#
