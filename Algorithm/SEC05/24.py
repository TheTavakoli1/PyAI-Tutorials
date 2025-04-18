_min = int(input('Enter your number1: '))
for i in range(9):
    number = int(input(f"Enter your number{i+2}: "))
    if number < _min:
        _min = number
print(_min, 'is the small number')   
