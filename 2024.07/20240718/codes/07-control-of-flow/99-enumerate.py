fruits = ['apple', 'banana', 'cherry']
# enumerate(iterable,start=0)

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)    