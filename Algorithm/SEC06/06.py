i = 1
while i <= 10:
    number = int(input(f"Enter Your number {i}: "))
    if number % 2 == 0:
        print(f'number is even')
    else:
        print(f'number is odd')
    i += 1
print('Done!')            