def welcome():
    print('''
Welcome to CALCULATOR
''')


welcome()


def calculate():
    # user inputs
    operation = str(input('''
    Please type the math operation you would like to complete:
    1 for Addition
    2 for Subtraction
    3 for Multiplication
    4 for Division
    __________________________________________________________
    '''))

    n1 = int(input('''
    ______________________
    Type the first number:
    '''))
    n2 = int(input('''
    ______________________
    Type the second number:
    '''))
    # invalid input

    # addition
    if operation == '1':
        print('''
        ___________________________
        You have selected Addition
        ___________________________
        ''')
        print('''
        ----------------------------
        The result of {} + {} is {}
        ----------------------------
        '''.format(n1, n2, n1 + n2))
    # subtraction
    elif operation == '2':
        print('''
        ______________________________
        You have selected Subtraction
        ______________________________
        ''')
        print('''
        ----------------------------
        The result of {} - {} is {}
        ----------------------------
        '''.format(n1, n2, n1 - n2))
    # multiplication
    elif operation == '3':
        print('''
        _________________________________
        You have selected Multiplication
        _________________________________
        ''')
        print('''
        ----------------------------
        The result of {} x {} is {}
        ----------------------------
        '''.format(n1, n2, n1 * n2))
    # division
    elif operation == '4':
        print('''
        __________________________
        You have selected Division
        __________________________
        ''')
        print('''
        ____________________________
        The result of {} / {} is {}
        ----------------------------
        '''.format(n1, n2, n1 / n2))

    # user error
    else:
        print('''
        _________________________________________________________________________________________________
        Error! You must select a numeric option between 1 and 4 in order to select the operation desired.
        __________________________________________________________________________________________________
        ''')

    again()


# Function to ask user if they want to use the calculator again
def again():
    # user input
    calc_again = input('''
---------------------------------
Do you want to calculate again?
Please type Y for YES or N for NO.
----------------------------------
''')
    # to use again
    if calc_again.upper() == 'Y':
        calculate()
    # to end the program and say goodbye to user
    elif calc_again.upper() == 'N':
        print('''
        ----------------------------------------------
        See you later. Thanks for using the calculator
        ----------------------------------------------
        ''')
    else:
        again()


calculate()
