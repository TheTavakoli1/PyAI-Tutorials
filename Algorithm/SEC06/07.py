i = 1
while i <= 10:
    number = int(input(f'Enter your number {i}:'))
    if 10 <= number < 100:
        print('Two-digit number')
    else:
        print('Not!')    
    i += 1    