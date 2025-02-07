# words = ["apple", "banana", "cherry", "date"]
# Use map() and a lambda to return a new list where each word is reversed.
# Expected Output: ["elppa", "ananab", "yrrehc", "etad"]

words = ["apple", "banana", "cherry", "date"]
result = list(map(lambda x : x[::-1], words))
print(result)