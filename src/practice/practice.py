from functools import reduce

l =[1,2,3,4,5]

s = reduce((lambda a,b : a+b),l)

print(s)
