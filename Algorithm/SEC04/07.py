#Swapping two Variables
number1 = int(input("Enter your number: "))
number2 = int(input("Enter your number: "))

print(f'Before Swapping: number1 = {number1} || number2 = {number2}')

#Swapping
number1, number2 = number2, number1

print(f'After Swapping: number1 = {number1} || number2 = {number2}')


