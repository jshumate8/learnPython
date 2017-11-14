name = raw_input("What is your name?")
age = raw_input("What is your age?")
favColor = raw_input("What is your favorite color?")

#message = name + age

message = "My name is {0}, my age is {1}, and my favorite color is {2}" .format(name, age, favColor)

#message = "My name is " + name + " and my age is " + age

print(message)