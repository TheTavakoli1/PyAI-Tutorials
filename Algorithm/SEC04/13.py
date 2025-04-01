# income = int(input("Enter your income: "))

# if income >= 50000000:
#     tax = income * 0.1
#     insurance = income * 0.1
#     total = income - tax - insurance
#     print(f"Tax: {tax}, Insurance: {insurance}, Total: {total}")

# elif 25000000 <= income < 50000000:
#     tax = income * 0.1
#     print(f"Tax: {tax}, total: {income - tax}")

# elif income < 25000000:
#     print(f"your finall income is {income}")

income = int(input("Enter your income: "))
fraction = 0.1
if income >= 50000000:
    print(f"tax = {fraction * income}, insurance = {fraction * income}, total = {income * 0.8}")

elif 25000000 <= income < 50000000:
    print(f" tax = {fraction * income}, total = {income * 0.9}")

else:
    print(f"your finall income is {income}")
    