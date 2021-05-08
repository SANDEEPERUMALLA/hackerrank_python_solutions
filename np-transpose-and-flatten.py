import numpy

m, n = list(map(int, input().split()))

lst = []
for i in range(0, m):
    lst.append(list(map(int, input().split())))

arr1 = numpy.array(lst)
print(arr1.transpose())
print(arr1.flatten())