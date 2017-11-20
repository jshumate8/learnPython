factors = {}
while True:
    get_out = raw_input("Hit 'q' to Quit or any other key to proceed. ")
    if get_out.lower() == 'q':
        print("Have a nice day!")
        break
    try:
        num = int(raw_input("Please input a number."))
        for num in range (1, num+1):
            factors[num]=num**2
        print factors
    except ValueError:
                print("Not a valid number.")

    