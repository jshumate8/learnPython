string1 = raw_input("What is the total amount?")
string2 = raw_input("What percentage of tip do you want to leave?")
num1 = float(string1)
num2 = float(string2)

result= (num1 * num2 *.01)
money= "${:,.2f}" .format(result)
message = "The tip amount is {0}" .format(money)
print message