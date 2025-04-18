_sum = 0
while True:
    number = int(input("Enter your number: "))
    _sum += number
    if number == 0:
        break

print(f'Sum of number: {_sum}')    