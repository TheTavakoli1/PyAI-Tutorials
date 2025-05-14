from functools import reduce

X = [1, 2, 3, 4, 5]
# for i in range(len(X)):
#     X[i] = X[i] * 2

# def product(num):
    # return num * 2

# lambda num:num*2

X = list(map(lambda num: num * 2, X))
# Y = list(filter(lambda num: num % 2 == 0, X))
sm = reduce(lambda x, y: x + y, X)
print(X)
# print(Y)
print(sm)