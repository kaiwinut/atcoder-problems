from math import sqrt

n = int(''.join(input().split()))

print('Yes' if int(sqrt(n)) == sqrt(n) else 'No')