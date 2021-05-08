import numpy

m, n = list(map(int, input().split()))

arr1 = numpy.array([list(map(int, input().split())) for _ in range(0, m)])
arr2 = numpy.array([list(map(int, input().split())) for _ in range(0, m)])

print(numpy.add(arr1, arr2))
print(numpy.subtract(arr1, arr2))
print(numpy.multiply(arr1, arr2))
print(numpy.floor_divide(arr1, arr2))
print(numpy.mod(arr1, arr2))
print(numpy.power(arr1, arr2))
