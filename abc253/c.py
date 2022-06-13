## Using heap
from heapq import heappop, heappush
from collections import Counter

Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

d = Counter()
A, B = [], []  # max, min in O(log N) time
for q in queries:
    if q[0] == 1:
        x = q[1]
        d[x] += 1
        heappush(A, x)
        heappush(B, -x)
    elif q[0] == 2:
        x, c = q[1:]
        d[x] -= min(c, d[x])
    else:
        # The zero-th element of a heap is always the smallest element
        while d[-B[0]] < 1:
            heappop(B)
        while d[A[0]] < 1:
            heappop(A)
        print(-B[0]-A[0]) 

# from collections import Counter

# Q = int(input())
# queries = [list(map(int, input().split())) for _ in range(Q)]

# s = Counter()
# min_key = 10 ** 10
# max_key = -1
# for q in queries:
#     if q[0] == 1:
#         s[q[1]] += 1
#         if q[1] < min_key:
#             min_key = q[1]
#         if q[1] > max_key:
#             max_key = q[1]
#     elif q[0] == 2:
#         s[q[1]] -= min(q[2], s[q[1]])
#         if s[q[1]] <= 0:
#             del s[q[1]]
#             if q[1] == min_key:
#                 min_key = 10 ** 10 if not s else min(s.keys())
#             if q[1] == max_key:
#                 max_key = -1 if not s else max(s.keys())
#     else:
#         print(max_key - min_key)