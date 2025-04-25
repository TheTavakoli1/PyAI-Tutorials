def pos_neg_zero(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


number = int(input("Enter a number: "))
print(pos_neg_zero(number))
