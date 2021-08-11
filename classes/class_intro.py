# class Dog:
#     animal_type = 'canine'
#
#     # Initialisation
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#         self.legs = 4
#
#     def bark(self):
#         return f"Woof! I am a {self.animal_type}"
#
#
# # Instantiation
#
# fido = Dog('Fido', 'Black')
# lassie = Dog("Lassie", 'Brown')
#
# print(fido.animal_type)
# print(lassie.animal_type)
#
# Dog.animal_type = 'arachnid'
#
# print(fido.legs)
# print(lassie.colour)
#
# Dog.legs = 8    # AFFECTS NOTHING IN DOGS - ONLY NEW INSTANCES
# print(fido.legs)
#
class Product:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand


class ShoppingCart:
    def __init__(self):
        self.__contents = []

    def add_to_cart(self, item: Product):
        self.__contents.append(item)

    def show_cart(self):
        for product in self.__contents:
            print(f"{product.name} from {product.brand}: £{product.price:.2f}")
        print()

    def get_cart_total(self):
        cart_total = 0.0
        for product in self.__contents:
            cart_total += product.price
        print(f"Total: £{cart_total:.2f}\n")
