import numpy

n,m = input().split(' ')

dimensions = []
for i in range(0, int(n)):
    dimensions.append(input().split(' ')) # m amount of values

_min = numpy.min(dimensions, axis=1)
_max = numpy.max(_min)
print(str(_max))