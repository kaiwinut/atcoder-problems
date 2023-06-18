n = int(input())
h = list(map(int, input().split()))

dp = [0] * n
dp[1] = abs(h[1] - h[0])

for i in range(2, n):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

cr = n-1
path = [cr+1]

while cr > 0:
    if dp[cr] == dp[cr-1] + abs(h[cr] - h[cr-1]):
        cr -= 1
    else:
        cr -= 2
    path.append(cr+1)

print(len(path))
print(*reversed(path))