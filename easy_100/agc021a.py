import math

n = int(input())

n2 = n
s = 0
while n2 > 0:
    s += (n2 % 10)
    n2 //= 10

d = int(math.log10(n))
f = n // (10 ** d)

print(max(f - 1 + 9 * d, s))