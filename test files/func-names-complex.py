# python file used to test function renaming,
# testing edge cases like import statements and 
# functions being redefined

a=5
b=10

def execute(r,s):
    return log(r,s)

def log(x, y):
    return x + y

var=log(a,b)
print(var) # 15

def log(left, right):
    return left - right

var=log(a,b)
print(var) # -5

import math as blah
var=log(a,b)
print(var) # -5

var=blah.log(a,b)
print(var) # 0.6989700043360187

from math import log as log, floor as bottom
var=log(a,b)
print(var) # 0.6989700043360187
print(bottom(a)) # 5

def log(left, right):
    return left - right

var=log(a,b)
print(var) # -5