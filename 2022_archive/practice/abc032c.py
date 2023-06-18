n,k = map(int, input().split())
s = [int(input()) for _ in range(n)]

if 0 in s:
    print(n)
    exit()

p = 0
m = 0
z = 1
for i in range(n):
    while p < n and z * s[p] <= k:
        z *= s[p]
        p += 1
    m = max(m, p-i)

    if p <= i: # if num larger than k, skip
        continue
    else:
        z //= s[i]

print(m)