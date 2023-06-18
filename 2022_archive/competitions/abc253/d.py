from math import gcd

N, A, B = map(int, input().split())

def sum_to_n(n):
    return n * (n + 1) // 2

sum_n = sum_to_n(N)
sum_a = A * sum_to_n(N // A)
sum_b = B * sum_to_n(N // B)

c = (A * B) // gcd(A, B)
sum_ab = c * sum_to_n(N // c)

print(sum_n - sum_a - sum_b + sum_ab)