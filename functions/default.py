def repeat_greeting(message="Hello!", number_of_times=3):   # have to define non-default parameters
    print(message * number_of_times)                        # before all optional parameters


repeat_greeting("eeee", 5)
repeat_greeting(" Hey there!")
repeat_greeting()
repeat_greeting(number_of_times=34)


class Dog:
    def __init__(self, name: str, legs: int = 4):
        self.name = name
        self.legs = legs


fido = Dog("Fido")
stool = Dog("Stool", 3)
print(fido.legs)
print(stool.legs)
