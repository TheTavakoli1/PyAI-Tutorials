number = int(input("Enter your number: "))
tens = number // 10
units = number % 10

if units % 2 == 0:
    print("units is even")
else:
    print("units is odd")

if tens % 2 == 0:
    print("tens is even")
    
else:
    print("tens is odd")
