# numbers = [5, 10, 15, 20, 25]
# Use map() and lambda to multiply each number by 2.
# Expected Output: [10, 20, 30, 40, 50]

numbers = [5, 10, 15, 20, 25]
result = list(map(lambda x : x*2, numbers))
print(result)
