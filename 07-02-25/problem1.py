# numbers = [1, 2, 3, 4, 5]
# Use the map() function with a lambda to square each number in the list.
# Expected Output: [1, 4, 9, 16, 25]


# def issquare(n):
#     return n*n


number = [1,2,3,4,5]
num = list(map(lambda x : x*x , number))
print(num)

