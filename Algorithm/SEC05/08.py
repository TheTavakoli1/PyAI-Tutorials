# print product of 10 numbers
_mul = 1
for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    _mul = _mul * number

print(f"The product of the numbers is {_mul}")
