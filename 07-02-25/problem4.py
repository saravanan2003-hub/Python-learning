# You have a list of words:
# words = ["apple", "banana", "kiwi", "grapes", "orange"]
# Use filter() and a lambda function to get only the words that have more than 5 letters.
# Expected Output: ["banana", "grapes", "orange"]

words = ["apple", "banana", "kiwi", "grapes", "orange"]
result = list(filter(lambda x : len(x)>5, words))
print(result)
