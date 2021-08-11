def important_function():
    print("I'm important!")

if __name__ == "__main__":
    print("I've been run directly!")
    important_function()
else:
    print("I've been imported!")
