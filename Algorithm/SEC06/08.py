_min = int(input('Enter your number1: '))
i = 1
while i <= 9:
    number = int(input(f'Enter your number{i+1}: '))
    if number < _min:
        _min = number
    i += 1

print(f'Min is: {_min}')        