import numpy

m, n = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(0, m)]
n_array = numpy.array(arr)
print(numpy.max(numpy.min(n_array, axis=1)))
