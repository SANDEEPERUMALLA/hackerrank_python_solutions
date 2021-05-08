n,x = map(int, input().split())
b = [map(float, input().split()) for i in range(x)]
for i in zip(*b):
    print(sum(i)/x)