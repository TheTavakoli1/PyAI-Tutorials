_sum = 0
for i in range(1, 11):
    number = int(input(f"Enter your number{i}: "))
    _sum = number + _sum

avarage = _sum / i
print(f'sum: {_sum}')    
print(f'avarage: {avarage}')