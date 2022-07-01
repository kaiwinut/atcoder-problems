n,l = map(int,input().split())
S = [input() for _ in range(n)]

S.sort()
ans = ''
for s in S:
    ans += s

print(ans)