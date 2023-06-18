N = int(input())
V = list(map(int, input().split()))

V.sort()

while len(V) > 2:
    a = V[0]
    b = V[1]
    V = [(a+b)/2] + V[2:]

print((V[0] + V[1])/2)