import numpy as np
random_array = np.random.randint(0, 100, (3, 3,))
print(random_array)

mean_value = np.mean(random_array)
print(mean_value)

median_value = np.median(random_array)
print(median_value)

variance_value = np.var(random_array)
print(variance_value)

standard_deviation_value = np.std(random_array)
print(standard_deviation_value)

min_value = np.min(random_array)
print(min_value)

max_value = np.max(random_array)
print(max_value)