n = int(input())
A = list(map(int, input().split()))

j=1
for a in A:
    if a==j:
        j += 1
if j > 1:
    print(n - j + 1)
else:
    print(-1)