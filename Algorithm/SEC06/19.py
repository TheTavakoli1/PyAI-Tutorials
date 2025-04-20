import os

while True:
    print("\n1. Sum")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Exit")

    operand = int(input("Enter your Choise: "))
    if operand == 1:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        os.system('clear')
        print(f"{number1} + {number2} = {number1 + number2}")

    elif operand == 2:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        os.system('clear')
        print(f"{number1} - {number2} = {number1 - number2}")

    elif operand == 3:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        os.system('clear')
        print(f"{number1} x {number2} = {number1 * number2}")

    elif operand == 4:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        os.system('clear')
        print(f"{number1} / {number2} = {number1 / number2}")

    elif operand == 5:
        break    
    os.system('clear')