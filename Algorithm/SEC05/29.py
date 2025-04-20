while True:
    number = int(input("Enter your number: "))
    counter = 0
    for i in range(1, number+1):
        if number % i == 0:
            counter += 1

    if counter > 2:
        print(f"{number} is not prime")
    else:
        print(f"{number} is prime")
    if number == -1:
        break             