## Easy solution
from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

dict_order = {}
for i, x in enumerate(permutations(range(1, N+1))):
    dict_order[x] = i

print(abs(dict_order[tuple(P)] - dict_order[tuple(Q)]))

## My solution

# from math import factorial

# N = int(input())
# P = list(map(int, input().split()))
# Q = list(map(int, input().split()))

# def get_idx_of_first(l):
#     if len(l) == 1:
#         return 1
#     cnt = 0
#     for v in l:
#         if v <= l[0]:
#             cnt += 1
#     return cnt

# a = 0
# b = 0
# while len(P) > 1 and len(Q) > 1:
#     a += (get_idx_of_first(P) - 1) * factorial(len(P) - 1)
#     b += (get_idx_of_first(Q) - 1) * factorial(len(Q) - 1)
#     P = P[1:]
#     Q = Q[1:]

# print(abs(b - a))