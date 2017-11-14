string1 = raw_input("Give me a number:")
string2 = raw_input("Now give me another number:")
num1 = float(string1)
num2 = float(string2)

result= num1 + num2
message = "The total of the two numbers is {0}" .format(result)
print message