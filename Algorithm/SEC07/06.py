def pass_fail(score):
    if score >= 10:
        return "Pass"
    else:
        return "Fail"

score = int(input("Enter your score: "))

print(pass_fail(score))
