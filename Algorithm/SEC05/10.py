# print even or odd number 10 times
for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")
