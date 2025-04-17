number1 = int(input(f'Enter your first numbe: '))
number2 = int(input(f'Enter your second numbe: '))

if number1 % 2 != 0:
    number1 = number1 + 1
    for i in range(number1, number2+1, 2):
        print(i)

else:
    for i in range(number1, number2, 2):
        print(i)        