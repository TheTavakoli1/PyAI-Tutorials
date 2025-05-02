# Data Structure
# List [] - ordered, mutable, allows duplicate elements - index - changeable

# names = list()
names = []

names.append("John")
names.append("Jane")
names.append("Jim")
names.append("Jill")
names.append("John")

# names[0] = 'Edit'
names.insert(2, 'New')
names.insert(len(names), 'End')
names.insert(0, 'Start')

print(names)
print(len(names))
print(type(names))

