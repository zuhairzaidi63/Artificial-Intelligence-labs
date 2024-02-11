def ADD(num1, num2):   # function for addition
    return num1 + num2


def SUB(num1, num2):  # function for subtraction
    return num1 - num2


def SQUARE(num1):   # function for square
    return num1 ** 2


def CUBE(num1):   # function for cube
    return num1 ** 3


flag = True
while flag == True:
    num1 = float(input("Enter 1st number "))    # taking 1st input
    num2 = float(input("Enter 2nd number "))     # taking 2nd input
    operator = input("Enter  any operator from + , - , ^2 , ^3 = ")  # ^2 is square and ^3 is cube
    if operator == "+":
        print(ADD(num1, num2))         # print sum of two numbers
    elif operator == "-":
        print(SUB(num1, num2))         # print subtraction of two numbers
    elif operator == "^2":
        print(SQUARE(num1), "is square of", num1)       # print square of two numbers separately
        print(SQUARE(num2), "is square of", num2)
    elif operator == "^3":
        print(CUBE(num1), "is square of", num1)          # print cube of two numbers separately
        print(CUBE(num2), "is square of", num2)
    else:
        print("ERROR INVALID OPERATOR")
    if int(input("Enter -1 for ending and any integer for continue : ")) == -1:
        break
    else:
        continue
