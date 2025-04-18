_sum = 0
count = 0
while True:
    number = int(input("Enter your number: "))
    if number == 0:
        break
    count += 1
    _sum += number

    
print(f"_sum of number is: {_sum}")
print(f"avarage number is {_sum/count}")    
