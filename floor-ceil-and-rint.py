import numpy
numpy.set_printoptions(legacy='1.13')
lst = list(map(float, input().split()))

arr = numpy.array(lst)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
