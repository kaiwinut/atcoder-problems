n = int(input())
a = list(map(int, input().split()))

p = 0
cnt = 0
for i in range(n):
    if p == i:
        p += 1
    while p < n and a[p] - a[p-1] > 0:
        p += 1
    cnt += p - i

print(cnt)