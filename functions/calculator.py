
def add(num1, num2):
    print("calculating addition:")
    return num1 + num2


def subtract(num1, num2):
    print("calculating subtraction:")
    return num1 - num2


def multiply(num1, num2):
    print("calculating multiplication:")
    return num1 * num2


def divide(num1, num2):
    print("calculating division:")
    if num2 == 0:
        return "Invalid - cannot divide by 0"
    else:
        return num1 / num2


# print("Please input the numbers to be used:")
# number1 = input("Number 1: ")
# number2 = input("Number 2: ")
# if not (num1.isdigit() and num2.isdigit()):
#     return "Please enter your numbers in digits"
# num1 = int(num1)
# num2 = int(num2)
#
# add_two_nums(number1, number2)
# subtract_two_nums(number1, number2)
# multiply_two_nums(number1, number2)
# divide_two_nums(number1, number2)

def calculator(instruction, int1, int2):
    if instruction == "add":
        return add(int1, int2)
    elif instruction == "subtract":
        return subtract(int1, int2)
    elif instruction == "multiply":
        return multiply(int1, int2)
    elif instruction == "divide":
        return divide(int1, int2)
    else:
        return "invalid instruction"
