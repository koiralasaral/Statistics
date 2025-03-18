# This script calculates Karl Pearson's coefficient of skewness for a given dataset
# Function to calculate the mode
def mode(x, f):
    max_frequency = max(f)
    mode_values = [x[i] for i in range(len(f)) if f[i] == max_frequency]
    return mode_values

# Function to calculate the mean, mode, and coefficient of skewness
def calculate_statistics(x, f):
    mean_val = mean(x, f)
    mode_val = mode(x, f)
    skewness = karl_pearson_skewness(x, f)
    return mean_val, mode_val, skewness
# Function to calculate the mean
def mean(x, f):
    n = sum(f)
    return sum(x[i] * f[i] for i in range(len(x))) / n



# Function to calculate the standard deviation
def standard_deviation(x, f, mean):
    n = sum(f)
    variance = sum(f[i] * (x[i] - mean) ** 2 for i in range(len(x))) / n
    return variance ** 0.5

# Function to calculate Karl Pearson's coefficient of skewness

def karl_pearson_skewness(x, f):
    n = sum(f)
    mean_val = mean(x, f)
    std_dev = standard_deviation(x, f, mean_val)
    skewness = sum(f[i] * ((x[i] - mean_val) / std_dev) ** 3 for i in range(len(x))) / n
    return skewness 


# Input from user
x = list(map(float, input("Enter the values of x (separated by spaces): ").split()))
f = list(map(int, input("Enter the frequencies (separated by spaces): ").split()))

# Calculate and print Karl Pearson's coefficient of skewness
skewness = calculate_statistics(x, f)
print(f"Karl Pearson's coefficient of skewness is: {skewness}")