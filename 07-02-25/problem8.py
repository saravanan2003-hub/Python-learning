# words = ["hello", "world", "python", "fastapi"]
# Use map() and a lambda to convert all words to uppercase.
# Expected Output: ["HELLO", "WORLD", "PYTHON", "FASTAPI"]

words = ["hello", "world", "python", "fastapi"]
result = list(map(lambda x : x.upper(), words))
print(result)