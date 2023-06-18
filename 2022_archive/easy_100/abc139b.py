from math import ceil


A, B = map(int, input().split())

# n :  ans
# A * n - n + 1 = (A - 1) n + 1 >= B
print(ceil((B - 1) / (A - 1)))