A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(M)]

min_price = min(a) + min(b)
for coupon in c:
    x, y, off = coupon
    if a[x-1] + b[y-1] - off < min_price:
        min_price = a[x-1] + b[y-1] - off

print(min_price)