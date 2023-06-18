n = int(input())

def check(x):  # if ans is lesser than or equals x
    if x ** 3 + x >= n:
        return True
    else:
        return False

l = 0
r = 100
eps = 10 ** -6

while l < r:
    m = (l + r) / 2
    if check(m):
        r = m - eps
    else:
        l = m + eps

print(l)