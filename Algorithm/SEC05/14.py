number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second numebr: "))

for i in range(number1, number2+1):
    print(i)
if number1 > number2:
    for i in range (number1, number2-1, -1):
        print(i)

print("Done!!!")                          