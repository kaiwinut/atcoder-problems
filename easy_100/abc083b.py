n,a,b = map(int, input().split())

s = 0
for i in range(1, n+1):
    x4 = i // 10000
    x3 = (i - x4 * 10000) // 1000
    x2 = (i - x4 * 10000 - x3 * 1000) // 100
    x1 = (i - x4 * 10000 - x3 * 1000 - x2 * 100) // 10
    x0 = i % 10
    if a <= x4 + x3 + x2 + x1 + x0 <= b:
        s += i

print(s)