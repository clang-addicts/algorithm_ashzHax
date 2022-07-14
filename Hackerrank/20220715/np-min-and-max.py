import numpy

n,m = input().split(' ')

for i in range(0,int(n)):
    dimensions = input().split(' ') # m amount of values

print(numpy.max(numpy.min(dimensions, axis=1)))