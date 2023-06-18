n = int(input())
a = list(map(int, input().split()))

p = 1
x = a[0]
s = a[0]
cnt = 0
for i in range(n):
    while p < n and x ^ a[p] == s + a[p]:
        x ^= a[p]
        s += a[p]
        p += 1

    cnt += p - i
    
    if p != i:
        x ^= a[i]
        s -= a[i]

print(cnt)