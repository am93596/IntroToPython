from class_intro import ShoppingCart, Product

cart = ShoppingCart()

cart.add_to_cart(Product("Chicken", 4.78, "Morrisons"))
cart.add_to_cart(Product("Bleach", 2.50, "ASDA"))
# cart.add_to_cart("turkey")
# cart.add_to_cart("kitchen sink")
cart.show_cart()
cart.get_cart_total()
cart.show_cart()