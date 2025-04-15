while True:
    # Initialize x
    x = ''
    while not (type(x) is float):
        try:
            # Enter x
            x = input('Type the 1st number(x) (Type "stop" to terminate the program): ')
            if x == "stop":
                break
            x = float(x)
        except ValueError:
            print('Try again\n')
            continue
    if x == "stop": break
    
    # Initialize y
    y = ''
    while not (type(y) is float):
        try:
            # Enter y
            y = input('Type the 2nd number(y) (Type "stop" to terminate the program): ')
            if y == "stop":
                break
            y = float(y)
        except ValueError:
            print('Try again\n')
            continue
    if y == "stop": break

    # Initialize math operation
    math_operations = ''
    while math_operations != '+' and math_operations != '-' and math_operations != '*' and math_operations != '/':
        # Enter math operation
        math_operations = input(
'''Type one of the the 4 math operations ("+"/"-"/"*"/"/")
+ (addition): x+y
- (subtraction): x-y
* (multification): x*y, 
/ (division): x/y
(Type "stop" to terminate the program): '''
        )

        # Calculation
        if math_operations == "stop": break
        elif math_operations == '+': print(x + y)
        elif math_operations == '-': print(x - y)
        elif math_operations == '*': print(x * y)
        elif math_operations == '/': print(x / y)
        else:
            print("Try again\n")
            continue
        break
    if math_operations == "stop": break

    continue