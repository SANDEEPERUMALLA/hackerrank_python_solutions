import numpy

m, n = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(0, m)]
n_array = numpy.array(arr)
print(numpy.mean(n_array, axis=1))
print(numpy.var(n_array, axis=0))
print(numpy.round(numpy.std(n_array, axis=None)))

#0.82915619759
#1.11803398875