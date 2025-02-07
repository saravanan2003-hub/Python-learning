# words = ["car", "bicycle", "train", "bus", "airplane"]
# Use filter() and a lambda to extract words with more than 4 letters.
# Expected Output: ["bicycle", "train", "airplane"]

words = ["car", "bicycle", "train", "bus", "airplane"]
result = list(filter(lambda x : len(x)>4, words))
print(result)