from itertools import accumulate

d = int(input())
n = int(input())

s = [0] * (d + 1)

for _ in range(n):
    l, r = map(int, input().split())

    s[l] += 1
    if r + 1 < len(s):
        s[r+1] -= 1

acc = list(accumulate(s))

for i in range(1, d+1):
    print(acc[i])