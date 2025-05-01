def absolute_value(number):
    if number < 0:
        return number * -1
    else:
        return number

number = int(input("Enter a number: "))

print(absolute_value(number))

