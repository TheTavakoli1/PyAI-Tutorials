def square(a, b):
    return f"Area: {a*b}", f"Premeter: {(a+b)*2}"

number1 = int(input("Enter your fisrt number: "))
number2 = int(input("Enter your second number: "))

area, perimeter = square(number1, number2)
print(area)
print(perimeter)