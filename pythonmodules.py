# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

#print(help("modules"))

#import math
#import math as m
#from math import pi

#print(math.pi)
#print(m.pi)
#print(pi)

#from math import e

#a, b, c, d = 1, 2, 3, 4
#print(e ** a)
#print(e ** b)
#print(e ** c)
#print(e ** d)

#import math

#a, b, c, d, e = 1, 2, 3, 4, 5
#print(math.e ** a)
#print(math.e ** b)
#print(math.e ** c)
#print(math.e ** d)
#print(math.e ** e)

pi = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2

import pythonmodules

result1 =  pythonmodules.pi
result2 =  pythonmodules.square(3)
result3 =  pythonmodules.cube(3)
result4 =  pythonmodules.circumference(3)
result5 =  pythonmodules.area(3)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)