# original function
for num in range(1, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz!")
    elif num % 3 == 0:
        print("Fizz!")
    elif num % 5 == 0:
        print("Buzz!")
    else:
        print(num)

# fizzbuzz that allows inputting of number, 'fizz', and 'buzz':
number = None
fizz = None
buzz = None
prompt_user = True
while prompt_user:
    print()
    number = input("Pick a number to start from, and I will print the results for the next 10 numbers!\n")
    print()
    if number.isdigit():
        number = int(number)
        prompt_user = False
    else:
        print("Please input an integer")
    fizz = input("Enter the word you want to appear instead of 'Fizz!'\n")
    buzz = input("Enter the word you want to appear instead of 'Buzz!'\n")

# Checks the next ten numbers from input number
for x in range(number, number+10):
    if (x % 3 == 0) and (x % 5 == 0):
        print(f"{fizz}{buzz}")
    elif x % 3 == 0:
        print(fizz)
    elif x % 5 == 0:
        print(buzz)
    else:
        print(x)
