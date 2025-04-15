_max = 0
for i in range(10):
    number = int(input(f"Enter your number{i+1}: "))
    if number > _max:
        _max = number

print(f"{_max} is the biggest number")        