# N, M, Q = map(int, input().split())
# queries = [list(map(int, input().split())) for _ in range(Q)]

# a = [[0] * M for _ in range(N)]
# fs = {1: [], 2:[]}
# for q in queries:
#     if q[0] == 1:
#         l, r, x = q[1:]
#         fs[1].append((l, r, x))
#         fs[2].append((-1, -1))
#     elif q[0] == 2:
#         i, x = q[1:]
#         fs[1].append((-1, -1, -1))
#         fs[2].append((i, x))
#     else:
#         ans = 0
#         i, j = q[1:]
#         for ifs in range(len(fs[1])):
#             if fs[1][ifs] == (-1,-1,-1):
#                 idx, x = fs[2][ifs]
#                 if i == idx:
#                     ans = x
#             elif fs[2][ifs] == (-1,-1):
#                 l, r, x = fs[1][ifs]
#                 if l <= j <= r:
#                     ans += x
#         print(ans)