N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

s = 0
for i in range(len(A)):
    k = 1 if i % 2 == 0 else -1
    s += k * A[i]

print(s)