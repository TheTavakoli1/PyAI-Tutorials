_min = 0
for i in range(10):
    number = int(input(f"Enter your number{i+1}: "))
    if number < _min:
        _min = number
print(_min, 'is the small number')   
