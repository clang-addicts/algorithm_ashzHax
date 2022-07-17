import numpy

if __name__ == '__main__':
    n,m = input().split(' ')

    dimensions = []
    for i in range(0, int(n)):
        arr = input().split(' ')
        t = []
        for j in arr:
            t.append(int(j))
        dimensions.append(t) # m amount of values

    _min = numpy.min(dimensions, axis = 1)
    _max = numpy.max(_min)
    print(str(_max))