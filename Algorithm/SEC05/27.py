space = 4
for i in range(1, 11, 2):
    print(space*" ", i*"*")
    space -= 1
space = 0
for i in range(9, -1, -2):
    print(space*" ", i*"*")
    space += 1    