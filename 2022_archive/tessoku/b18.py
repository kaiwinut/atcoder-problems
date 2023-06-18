n,s = map(int,input().split())
a = [0] + list(map(int,input().split()))

dp = [[0] * (s+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(s+1):
        if j - a[i] < 0:
            if dp[i-1][j] == 1:
                dp[i][j] = 1
        else:
            if dp[i-1][j] == 1 or dp[i-1][j - a[i]] == 1:
                dp[i][j] = 1

if dp[n][s] == 0:
    print(-1)
    exit()

ci = n
cj = s
cards = []
while cj > 0:
    if cj - a[ci] >= 0 and dp[ci-1][cj - a[ci]] == 1:
        cards.append(ci)
        cj -= a[ci]
    ci -= 1

print(len(cards))
print(*reversed(cards))