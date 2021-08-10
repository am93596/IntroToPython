prompt_user = True

while prompt_user:
    age = input("What is your age?\t")
    if age.isdigit():
        if int(age) < 120:
            age = int(age)
            prompt_user = False
        else:
            print("Don't be silly!")
    else:
        print("Please provide age in digits")
