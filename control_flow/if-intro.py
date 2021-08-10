# IF
#
# age = 14
#
# if age >= 15:
#     print("You can watch this slightly violent film.")
#     print("This is still in the if statement block")
#     print("Still part of the if-block")
# elif age == 14:
#     print("Come back next year")
# else:
#     print("You are too young to watch this slightly violent film")
#
# print("This will always run")
#
# film_rating = "15"
#
# if film_rating == "U":
#     print("All age groups can watch this film")
# elif film_rating == "PG":
#     print("You can only watch this if you are supervised by adults")
# elif film_rating == "12A":
#     print("You can only watch this if you are 12 or over")
# elif film_rating == "15":
#     print("You can only watch this if you are 15 or over")
# else:
#     print("You can only watch this if you are 18 or over")

# Kieron's Code

# age = input("What is the film rating? U, PG, 12A, 15, 18?:\n")
#
# if age.upper() == "U":  Something that will be resolved true or false followed by :
#     print("Everyone can watch this!")
# elif age.upper() == "PG":
#     print("If you're under 15, You need a Parent!")
# elif age.upper() == "12A":
#     print("If you're 12 you're fine!")
# elif age == "15":
#     print(" You have to be 15 to watch this movie!")
# elif age == "18":
#     print("Being 18+, Go enjoy all the films")
# else:
#     print("Please specify the correct film rating: U, PG, 12A, 15, or 18!")
# END Kieron's code

age = None
film_cert = None
restriction_message = "You are too young to watch this film"
go_ahead_message = "You can watch this film"

prompt_user_for_age = True
while prompt_user_for_age:
    age = input("What is your age?\t")
    if age.isdigit():
        if int(age) < 120:
            age = int(age)
            prompt_user_for_age = False
        else:
            print("Don't be silly!")
    else:
        print("Please input your age as an integer")

validCertList = ["U", "PG", "12A", "15", "18"]
prompt_user_for_cert = True
while prompt_user_for_cert:
    film_cert = input("What is the film rating?\t")
    if film_cert.upper() in validCertList:
        film_cert = film_cert.upper()
        prompt_user_for_cert = False
    else:
        print("Please input the correct film rating: U, PG, 12A, 15, or 18")

print("Loading...")

if film_cert == "U":
    print("You can watch this film")
elif film_cert == "PG":
    if age >= 18:
        print("You can watch this film")
    else:
        print("You can only watch this if you are supervised by adults")
elif film_cert == "12A":
    if age >= 12:
        print("You can watch this film")
    else:
        print("You are too young to watch this film")
elif film_cert == "15":
    if age >= 15:
        print("You can watch this film")
    else:
        print("You are too young to watch this film")
else:
    if age >= 18:
        print("You can watch this film")
    else:
        print("You are too young to watch this film")
