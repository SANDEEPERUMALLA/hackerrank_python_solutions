import numpy

n = int(input())

arr1 = [list(map(int, input().split())) for _ in range(0, n)]
arr2 = [list(map(int, input().split())) for _ in range(0, n)]

A = numpy.array(arr1)
B = numpy.array(arr2)
print(numpy.dot(A, B))
