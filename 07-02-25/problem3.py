# celsius = [0, 10, 20, 30, 40]
# Use map() and lambda to get [32.0, 50.0, 68.0, 86.0, 104.0]

celsius = [0,10,20,30,40]
result = list(map(lambda x: (x*9/5)+32, celsius ))
print(result)