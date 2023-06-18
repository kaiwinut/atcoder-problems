n = int(input())
a = [0] + list(map(int, input().split()))
b = [0, 0] + list(map(int, input().split()))

dp = [0] * n
dp[1] = a[1]

for i in range(2, n):
    dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i])

cr = n - 1
path = [cr+1]

while cr > 0:
    if dp[cr] == dp[cr-1] + a[cr]:
        cr -= 1
    else:
        cr -= 2
    path.append(cr+1)

print(len(path))
print(*reversed(path))