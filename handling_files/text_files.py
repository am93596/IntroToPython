import os

parent_dir = os.path.dirname(__file__)
# filepath = os.path.join(parent_dir + "\\order.txt")
# file = open(os.path.join(parent_dir + "\\order.txt"))
# data = file.read()  # All the data as a string
# data = file.readline()  # Next line in the buffer as a string
# data = file.readlines()
# data = [order.strip('\n') for order in file.readlines()]
# data = list(map(lambda x: x.strip('\n'), file.readlines()))
# print(data)
# file.close()

# Context Manager
# try:
#     with open(filepath, 'r') as file:
#         data = list(map(lambda x: x.strip('\n'), file.readlines()))
# except FileNotFoundError as errmsg:
#     print("Could not find the right file", errmsg)
# finally:
#     print("This will happen if there is or isn't an error")

# r = Open for reading
# w = Open for writing *
# x = exclusive creation - doesn't work if file already exists
# a = Open for writing - appends to end of file if file already exists
# t = text mode (can be combined with above)
# b = binary mode (can be combined with above)
# + = open for updating (reading and writing)


# def add_order_to_file(filepath, order_item):
#     try:
#         with open(filepath, 'a') as file:
#             file.write(order_item + '\n')
#     except FileNotFoundError:
#         print("Get the file path right, you fool!")
#         raise
#
#
# add_order_to_file(filepath, 'Eggs on Toast')
# add_order_to_file(filepath, 'Quiche')

# Read from a drinks order file (e.g. drinks_order.txt)
# Check that each drink in the order is available
# in the drinks_menu.txt
# What should happen if it isn't?

order_filepath = os.path.join(parent_dir + "\\drinks_order_new.txt")
menu_filepath = os.path.join(parent_dir + "\\drinks_menu.txt")


def is_item_in_menu(order, menu):
    try:
        with open(order) as file:
            order_items = list(map(lambda x: x.strip('\n'), file.readlines()))
        with open(menu) as file:
            menu_items = list(map(lambda x: x.strip('\n'), file.readlines()))
    except FileNotFoundError:
        print("Please put in the correct file path.\n")

    for item in order_items:
        if item in menu_items:
            print(f"{item} is available!\n")
            with open('receipt.txt', 'a') as file:
                file.write(item + '\n')
        else:
            print(f"Sorry, {item} is not available.\n")
    return "Great! Your order is being processed.\n"


print(is_item_in_menu(order_filepath, menu_filepath))
