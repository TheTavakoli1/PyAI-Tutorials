number = int(input("Enter your number: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1

print(f"Factorial: {factorial}")