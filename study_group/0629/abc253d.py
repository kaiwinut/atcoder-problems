from math import gcd

n, a, b = map(int, input().split())

def get_sum(x, num):
    return x * num * (num + 1) // 2

a_sum = get_sum(a, n//a)
b_sum = get_sum(b, n//b)

g = gcd(a, b)
c = (a // g) * (b // g) * g
c_sum = get_sum(c, n//c)

print(get_sum(1, n) - a_sum - b_sum + c_sum)