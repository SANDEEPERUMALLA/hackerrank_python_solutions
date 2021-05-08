import numpy

n, m, p = list(map(int, input().split()))

arr1 = [list(map(int, input().split())) for i in range(0, n)]
arr2 = [list(map(int, input().split())) for j in range(0, m)]

print(numpy.concatenate((arr1, arr2)))
