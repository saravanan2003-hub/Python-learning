# numbers = [10, 15, 20, 30, 35, 45, 50, 60]
# Use filter() and a lambda function to get numbers divisible by both 3 and 5.
# Expected Output: [15, 30, 45, 60]

numbers = [10, 15, 20, 30, 35, 45, 50, 60]
result = list(filter(lambda x : x%5==0 and x%3==0, numbers))
print(result)
