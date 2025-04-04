# Divisible by 3 or 5
for i in range(1, 11):
    number = int(input(f'Enter number {i}: '))
    if number % 3 == 0 or number % 5 == 0:
        print(f'{number} is divisible by 3 or 5')
    else:
        print(f'{number} is not divisible by 3 or 5')
