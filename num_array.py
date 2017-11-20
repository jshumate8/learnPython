def doubled(i):
    for i in range(0,len(numbers)):
        print(numbers[i],  "x2 =", + numbers[i]*2)

numbers = [1, 2, 5, 10, 12, 15, 18, 345, 821]
numbers.append(99)
del numbers[-3]
print(numbers)
doubled(numbers)
