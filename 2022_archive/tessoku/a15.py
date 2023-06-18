n = int(input())
a = list(map(int, input().split()))

s = list(set(a))
s.sort()
d = {s[i]: i+1 for i in range(len(s))}

ans = []
for e in a:
    ans.append(d[e])

print(*ans)