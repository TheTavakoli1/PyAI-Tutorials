# Print name and family with 10 spaces between them
name = input("Enter your name: ")
family = input("Enter your family: ")

print(name + " " * 10 + family)

print(name, family, sep=" " * 10)

print(f"{name}{' ' * 10}{family}")

print(name + "         " + family)
