while True:
    number = int(input("Enter your number: "))
    counter = 0
    i = 1
    while i <= number:
        if number % i == 0:
            counter += 1
        i += 1    

    if counter > 2:
        print(f"{number} is not Prime")
    else:
        print(f"{number} is prime")            

