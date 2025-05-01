def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    

number1 = int(input("Enter a number: "))
operator = input("Enter an operator (+, -, *, /): ")
number2 = int(input("Enter a number: "))

print(calculator(number1, number2, operator))

