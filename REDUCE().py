# reduce(function, collection)= Reduces elements in a collection to a single value
#                               For loop is better in most cases
#                               Reduce is better for a functional approach + readability

from functools import reduce

#def add(x, y):
#    return x + y

prices = [20.00, 59.50, 102.42, 5.00, 320.99]

#total = reduce(add, prices)
#print(f"Rs{total}")

#OR
total = reduce(lambda x,y: x+y, prices)
print(f"Rs{total}")