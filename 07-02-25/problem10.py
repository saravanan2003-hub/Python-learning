# numbers = [1, 2, 3, 4, 5]
# Use map() and a lambda to return a new list with cubes of each number.
# Expected Output: [1, 8, 27, 64, 125]

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x : x**3, numbers))
print(result)