import numpy


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

A = numpy.array(arr1)
B = numpy.array(arr2)
print(numpy.inner(A, B))
print(numpy.outer(A, B))

