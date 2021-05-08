import re

m, n = list(map(int, input().rstrip().split()))
mat = []
for _ in range(m):
    mat.append(input())

decodedString = ''
for j in range(0, n):
    for i in range(0, m):
        decodedString += mat[i][j]

result = re.sub(r'(?<=[0-9a-zA-Z])([^0-9a-zA-Z]+)(?=[0-9a-zA-Z])', ' ', decodedString)
print(result)
