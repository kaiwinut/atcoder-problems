from math import ceil
x = int(input())

s = x % 100
n = x // 100

cnt = ceil(s / 5)

print(1 if n >= cnt else 0)