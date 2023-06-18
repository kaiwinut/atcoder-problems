n, q = map(int,input().split())

s = [0] * n

for _ in range(q):
    l, r = map(int,input().split())
    for i in range(l-1, r):
        if s[i] == 0:
            s[i] = 1
        else:
            s[i] = 0

print(sum(s))