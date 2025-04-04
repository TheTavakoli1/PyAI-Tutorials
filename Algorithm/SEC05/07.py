# print sum of 10 numbers
_sum = 0
for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    _sum = _sum + number

print(f"The sum of the numbers is {_sum}")
