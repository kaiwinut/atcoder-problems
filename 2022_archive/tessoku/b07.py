from itertools import accumulate


t = int(input())
n = int(input())

a = [0] * (t + 2)

for _ in range(n):
    l, r = map(int, input().split())

    # 前時刻よりどれくらい増えたか
    a[l] += 1
    a[r] -= 1

acc = list(accumulate(a))

for i in range(1, t+1):
    print(acc[i-1])