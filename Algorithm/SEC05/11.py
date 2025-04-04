# print even or odd number 10 times and count even and odd numbers
even = 0
odd = 0

for i in range(1, 11):
    number = int(input(f"Enter your number {i}: "))
    if number % 2 == 0:
        print(f"Number {number} is even")
        even += 1
    else:
        print(f"Number {number} is odd")
        odd += 1

print(f"There are {even} even numbers and {odd} odd numbers")

