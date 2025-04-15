x = ''
y = ''

while x == str(x) or y == str(y):
    try:
        x = input('Type the 1st number(x): ')
        y = input('Type the 2nd number(y): ')

        x = float(x)
        y = float(y)

        math_operations = ''

        while math_operations != 'add' and math_operations != 'sub' and math_operations != 'mul' and math_operations != 'div':

            try:
                math_operations = input(
                    'Type one of the the 4 math operations (add/sub/mul/div)\nadd(addition): x+y, sub(subtraction): x-y\nmul(multification): x*y, div(division): x/y\n(If this text appear again, please try again.): '
                    '')

                if math_operations == 'add':
                    print(x + y)
                if math_operations == 'sub':
                    print(x - y)
                if math_operations == 'mul':
                    print(x * y)
                if math_operations == 'div':
                    print(x / y)
            except:
                continue
        continue
    except ValueError:
        print('Try again')
        continue