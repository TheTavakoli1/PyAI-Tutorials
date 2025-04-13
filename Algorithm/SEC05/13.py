for i in range(1, 5):
    income = int(input(f"Enter your income{i}: "))
    tax =  income * 0.1
    print(f"10% tax: {tax}")
    insurance = income * 0.1
    print(f"10% insurance: {insurance}")
    print(f"Your finall income: {income * 0.8}")  