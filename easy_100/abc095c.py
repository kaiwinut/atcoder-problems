a,b,c,x,y = map(int, input().split())

p1 = 10 ** 10
p2 = 10 ** 10

if x >= y:
    p1 = 2 * c * y + a * (x - y)

else:
    p2 = 2 * c * x + b * (y - x)

p3 = 2 * c * max(x, y)

p4 = a * x + b * y

print(min(p1, p2, p3, p4))