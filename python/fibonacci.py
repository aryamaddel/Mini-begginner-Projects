a = 0
b = 1
result = '0, 1'
for i in range(1000):
    sum = a+b
    result += ', ' + str(sum)
    a = b
    b = sum


print(result)
