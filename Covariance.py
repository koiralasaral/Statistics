import numpy as np
import matplotlib.pyplot as plt

def calculate_covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length")
    
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    return covariance

def calculate_pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length")
    
    covariance = calculate_covariance(x, y)
    std_x = np.std(x)
    std_y = np.std(y)
    
    return covariance / (std_x * std_y)

# Example usage

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
print(f"Covariance: {calculate_covariance(x, y)}")
print(f"Pearson Correlation Coefficient: {calculate_pearson_correlation(x, y)}")

# Plotting the covariance and Pearson correlation coefficient
father_heights = [65, 66, 67, 68, 69, 70, 71]
son_heights = [67, 68, 66, 69, 72, 72, 69]

covariance = calculate_covariance(father_heights, son_heights)
pearson_correlation = calculate_pearson_correlation(father_heights, son_heights)
print(f"Covariance: {covariance}")
print(f"Pearson Correlation Coefficient: {pearson_correlation}")

plt.scatter(father_heights, son_heights)
plt.title(f'Father vs Son Heights\nPearson Correlation Coefficient: {pearson_correlation:.2f}')
plt.xlabel('Father Heights (cm)')
plt.ylabel('Son Heights (cm)')
plt.show()
