n = int(input())
MAX = 1500

p = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for _ in range(n):
    x, y = map(int, input().split())
    p[x][y] += 1

s = [[0] * (MAX + 1) for _ in range(MAX + 1)]
for i in range(len(s)):
    for j in range(1, len(s[0])):
        s[i][j] = s[i][j-1] + p[i][j]
for i in range(1, len(s)):
    for j in range(len(s[0])):
        s[i][j] = s[i-1][j] + s[i][j]

q = int(input())
for _ in range(q):
    a,b,c,d = map(int, input().split())
    print(s[c][d] + s[a-1][b-1] - s[c][b-1] - s[a-1][d])