a, b, c = map(int, input().split())

s = sorted([a, b, c])

if b == s[1]:
    print('Yes')
else:
    print('No')