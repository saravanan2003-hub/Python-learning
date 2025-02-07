# Given a list of numbers, filter out the even numbers using the filter() function and a lambda.
# numbers = [10, 15, 20, 25, 30, 35]
# Expected Output: [15, 25, 35]

numbers = [10, 15, 20, 25, 30, 35]
result = list(filter(lambda x : x%2!=0, numbers))
print(result)





