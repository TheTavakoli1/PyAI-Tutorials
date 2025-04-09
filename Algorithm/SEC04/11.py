# int square root

number = int(input("Enter your number: "))
square_root = number ** 0.5
print(f'Square Root of {number} is {square_root}')

if square_root == int(square_root):
    print("Perfect Square")
else:
    print("Not a Perfect Square")

