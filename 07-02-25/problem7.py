# numbers = [12, 15, 18, 21, 24, 27, 30]
# Use filter() and a lambda function to extract only the odd numbers.
# Expected Output: [15, 21, 27]

numbers = [12, 15, 18, 21, 24, 27, 30]
result = list(filter(lambda x : x%2!=0, numbers))
print(result)
