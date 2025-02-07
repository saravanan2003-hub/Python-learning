# names = ["Ajay", "Bala", "Arun", "Deepak", "Akash", "Charan"]
# Use filter() and a lambda function to get only the names that start with 'A'.
# Expected Output: ["Ajay", "Arun", "Akash"]

names = ["Ajay", "Bala", "Arun", "Deepak", "Akash", "Charan"]
result = list(filter(lambda x : x[0]=="A", names))
print(result)