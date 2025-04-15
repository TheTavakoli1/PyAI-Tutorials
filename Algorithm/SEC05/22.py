# number = int(input("Enter your numebr: "))

# for i in range(number-1, 1, -1):
#     number = number * i

# print(number)   


number = int(input("Enter you number: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i 

print(factorial)    