# km_distances = [1, 5, 10, 20, 50]
# Use map() and a lambda to convert these distances to miles.
# Formula:
# miles = km × 0.621371
# miles= km × 0.621371
# Expected Output: [0.62, 3.11, 6.21, 12.43, 31.07] (approx values)

import math

km_distances = [1, 5, 10, 20, 50]
result = list(map(lambda x : round(x *0.621371,2), km_distances))
print(result)
