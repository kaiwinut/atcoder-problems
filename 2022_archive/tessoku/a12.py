n,k = map(int, input().split())
a = list(map(int, input().split()))

def check(x): # if ans is below or equal x seconds
    s = 0
    for r in a:
        s += x // r
    if s >= k:
        return True
    return False

l = 1
r = 10 ** 9

while l < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m + 1

print(l)