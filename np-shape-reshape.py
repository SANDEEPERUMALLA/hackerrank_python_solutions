import numpy

i_list = list(map(int, input().split()))
arr1 = numpy.array(i_list)
changed_array = numpy.reshape(arr1, (3,3))
print(changed_array)