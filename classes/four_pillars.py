# Four Pillars

# Abstraction - use methods to make life easier for the end user
# Encapsulation - hide away dangerous things
# Inheritance
# Polymorphism

# class Animal:
#     def __init__(self):
#         self.alive = True
#
#     def hunt(self):
#         print("Searching for food")
#
#     def move(self):
#         print("Moving...")
#
#
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breed(self):
#         print("Giving birth to live young")
#
#
# class Platypus(Mammal):
#     def __init__(self):
#         super().__init__()
#
#     def breed(self):
#         print("Laying eggs")
#
#
# perry = Platypus()
# perry.breed()
# m = Mammal()
# m.breed()

# METHOD OVERLOADING (Polymorphism)
# def add(int1, int2):
#     return int1 + int2
#
# def add(int1, int2, int3):
#     return int1 + int2 + int3
#
# print(add(1, 2))
# print(add(1, 2, 3))
# Doesn't work in Python, but exists in other languages

# class Reptile(Animal):
#     def __init__(self, reptile_type, colour):
#         super().__init__()
#         self.reptile_type = reptile_type
#         self.colour = colour
#
#
# class Snake(Reptile):
#     def __init__(self, colour):
#         super().__init__("Snake", colour)
#
#
# s = Snake("Green")
# print(s.alive)
# s.hunt()
# s.move()
# print(s.reptile_type)
#
# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def get_area(self):
#         return self.width * self.length
#
#     def get_length(self):
#         return self.length
#
#
# class BlueThings:
#     def __init__(self):
#         self.colour = "Blue"
#
#
# class BlueSquare(Rectangle, BlueThings):
#     def __init__(self, length):
#         Rectangle.__init__(self, length, length)
#         BlueThings.__init__(self)
#

# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, len())
#
#
# s = BlueSquare(10)
# print(s.colour)
# print(s.get_area())

# Scrabble Checker Object
# Initialise it with a string of 7 random letters - Done!
    # Option of providing some letters, and the rest randomly generated
# A method to check that a submitted word can be made from those tiles
# A method to return the score for a submitted word
# A method to use the methods above to check a word is valid
# and if it is, return the score for that word
import random


class ScrabbleChecker:
    def __init__(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        list_of_random_letters = random.choices(alphabet, k=7)
        self.random_letters = ''.join(list_of_random_letters)


sc = ScrabbleChecker()
print(sc.random_letters)
