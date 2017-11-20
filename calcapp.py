import calculator as c

while True:
    get_out = raw_input("Hit 'q' to Quit or any other key to proceed. ")
    if get_out.lower() == 'q':
        print("Have a nice day!")
        break
    else: 
        while True:
            try:
                firstNum = int(raw_input("Please give me the first number: "))
                break
            except ValueError:
                print("Not a valid number.")
    
    while True:
        operation = raw_input("Hit + to add, - to subtract, * to multiply, or / to divide: ")
        if operation in ('+', '-', '*', '/'): 
            break
        else:
            print("Invalid Input")

    while True:
            try:
                secondNum = int(raw_input("Please give me the second number: "))
                break
            except ValueError:
                print("Not a valid number.")

    firstNum = int(firstNum)
    secondNum = int(secondNum)

    if operation == '+':
        answer = c.add(firstNum, secondNum)
        
    elif operation == '-':
        answer = c.subtract(firstNum, secondNum)
        
    elif operation == '*':
        answer = c.multiply(firstNum, secondNum)   

    elif operation == '/':
        try:
            answer = c.divide(firstNum, secondNum)
        except ZeroDivisionError:
            print "You can't divide by zero!"
            break
     

