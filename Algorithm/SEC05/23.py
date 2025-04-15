for i in range(10):
    number = int(input(f"Enter you number{i+1}: "))
    if number == 0:
        print("Zero!")
    elif number > 0:
        print("Pozitive")
    elif number < 0:
        print("Negative")      

print("Done!")          