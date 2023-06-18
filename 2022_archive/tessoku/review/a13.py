n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
r = 0

for l in range(n):
    while r < n - 1 and a[r+1] - a[l] <= k:
        r += 1
    
    cnt += r - l

print(cnt)