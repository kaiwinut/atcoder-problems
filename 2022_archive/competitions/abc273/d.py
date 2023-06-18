from bisect import bisect_left
from collections import defaultdict

h,w,rs,cs = map(int,input().split())
n = int(input())
rc = [list(map(int,input().split())) for _ in range(n)]
q = int(input())
dl = [list(input().split()) for _ in range(q)]

row_obs = defaultdict(list)
col_obs = defaultdict(list)

for r, c in sorted(rc, key=lambda x: (x[0], x[1])):
    row_obs[r].append(c)

for r, c in sorted(rc, key=lambda x: (x[1], x[0])):
    col_obs[c].append(r)

direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for d, l in dl:
    length = int(l)
    new_r, new_c = rs + direction[d][0] * length, cs + direction[d][1] * length

    if d == 'L':
        obs = row_obs[rs]
        index_s = bisect_left(obs, cs)
        # print(obs, (index_s, index_e), (rs, cs), (new_r, new_c))
        if index_s == 0:
            cs = new_c
        else:
            cs = max(obs[index_s - 1] + 1, new_c)

    elif d == 'R':
        obs = row_obs[rs]
        index_s = bisect_left(obs, cs)
        if index_s == len(obs):
            cs = new_c
        else:
            cs = min(obs[index_s] - 1, new_c)

    elif d == 'U':
        obs = col_obs[cs]
        index_s = bisect_left(obs, rs)
        if index_s == 0:
            rs = new_r
        else:
            rs = max(obs[index_s - 1] + 1, new_r)

    elif d == 'D':
        obs = col_obs[cs]
        index_s = bisect_left(obs, rs)
        if index_s == len(obs):
            rs = new_r
        else:
            rs = min(obs[index_s] - 1, new_r)

    rs = min(h, rs)
    rs = max(1, rs)
    cs = min(w, cs)
    cs = max(1, cs)

    print(rs, cs)